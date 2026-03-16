import ollama
import json
import re

class ParserCurgicoIA:
    def __init__(self):
        self.model = 'llama3.1'

    def separar_bits(self, raw_hex):
        """
        Corte manual baseado na anatomia do protocolo GT06.
        Dessa forma, a IA não precisa adivinhar onde os dados começam.
        """
        # Garantimos que a string tenha o tamanho mínimo esperado
        if len(raw_hex) < 44:
            return None

        # Fatiamento fixo (Offsets)
        fatias = {
            "header": raw_hex[0:4],           # 78 78
            "length": raw_hex[4:6],           # Tamanho
            "protocol_id": raw_hex[6:8],      # Tipo de pacote (12 = Localização)
            "datetime_hex": raw_hex[8:20],    # Data e Hora
            "satellites": raw_hex[20:22],     # Satélites
            "latitude_hex": raw_hex[22:30],   # Latitude (4 bytes)
            "longitude_hex": raw_hex[30:38],  # Longitude (4 bytes)
            "speed_hex": raw_hex[38:40],      # Velocidade
            "course_status": raw_hex[40:44],  # Status e Direção
            "serial_number": raw_hex[44:48],  # Serial da mensagem
            "error_check": raw_hex[48:52] if len(raw_hex) > 48 else "N/A"
        }
        return fatias

    def traduzir_com_ia(self, fatias):
        """
        Envia os pedaços já cortados para a IA converter em dados legíveis.
        """
        prompt = f"""
        Você é um conversor de telemetria. Receba os pedaços HEX já fatiados e converta:
        
        DADOS FATIADOS:
        {json.dumps(fatias, indent=2)}
        
        REGRAS DE CONVERSÃO:
        1. Latitude/Longitude: Converta de HEX para Decimal. No GT06, divida o valor decimal por 1.800.000 (ou conforme escala de graus).
        2. Velocidade: Converta HEX para Decimal (km/h).
        3. Status: Identifique se a ignição está ligada (bit de status).
        
        Retorne APENAS o JSON final com os dados convertidos.
        """

        try:
            response = ollama.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            
            conteudo = response['message']['content']
            json_match = re.search(r'\{.*\}', conteudo, re.DOTALL)
            return json.loads(json_match.group()) if json_match else None
        except Exception as e:
            print(f"Erro na tradução: {e}")
            return None

# --- EXECUÇÃO DO PROCESSO ---

def processar_rastreador(string_hex):
    parser = ParserCurgicoIA()
    
    print(f"1. Iniciando fatiamento da string: {string_hex}")
    fatias = parser.separar_bits(string_hex)
    
    if fatias:
        print("2. String separada com sucesso. Enviando para Tradução IA...")
        resultado = parser.traduzir_com_ia(fatias)
        
        if resultado:
            print("\n" + "="*50)
            print("DADOS DECODIFICADOS DA PLATAFORMA")
            print("="*50)
            print(json.dumps(resultado, indent=4, ensure_ascii=False))
            print("="*50)
        else:
            print("Erro ao traduzir dados.")
    else:
        print("String inválida ou muito curta.")

# String de exemplo (GT06 Location Packet)
string_exemplo = "78781F120B081D112E1FCC0271D0A20668CB00017500010D0A"
processar_rastreador(string_exemplo)