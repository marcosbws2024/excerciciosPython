import ollama
import psycopg2
import json
import re
from psycopg2.extras import Json

class ParserInteligenteIA:
    def __init__(self):
        self.model = "llama3.1"
        self.db_params = {
            "dbname": "RASTREAR",
            "user": "postgres",
            "password": "123",
            "host": "localhost"
        }

    def _get_system_prompt(self):
        """Define a inteligência de engenharia da IA."""
        return """
        Você é um Analista Sênior de Protocolos de Telemetria.
        Sua missão é decompor strings brutas (HEX/ASCII) e extrair a lógica de fatiamento.
        
        REGRAS DE ANÁLISE:
        1. Identifique o tamanho da string e se ela está completa.
        2. Localize o cabeçalho (ex: 7878=GT06, +RESP=Suntech, 0000=Teltonika).
        3. Fatie a string campo a campo (Ex: Header, ID, Payload, CRC).
        4. Converta valores técnicos:
           - Latitude/Longitude para Graus Decimais.
           - Status de Bits para Boolean (Ignição On/Off).
        
        RETORNO OBRIGATÓRIO (JSON):
        {
            "metadata": {"protocolo": "string", "tamanho_valido": bool},
            "anatomia": {"segmento_hex": "significado técnico"},
            "plataforma": {
                "id": "string", 
                "lat": float, 
                "lng": float, 
                "vel": float, 
                "ign": bool,
                "status": "string"
            }
        }
        """

    def interpretar(self, raw_hex):
        """Chama o Llama 3.1 local para processar a string."""
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': self._get_system_prompt()},
                    {'role': 'user', 'content': f"Analise detalhadamente: {raw_hex}"}
                ]
            )
            
            # Limpeza de resposta para garantir JSON puro
            raw_content = response['message']['content']
            json_match = re.search(r'\{.*\}', raw_content, re.DOTALL)
            
            if json_match:
                return json.loads(json_match.group())
            return None
        except Exception as e:
            print(f"Erro na IA: {e}")
            return None

    def salvar(self, raw_hex, analise):
        """Insere a inteligência e os dados no PostgreSQL."""
        if not analise: return

        try:
            conn = psycopg2.connect(**self.db_params)
            cur = conn.cursor()
            
            p = analise['plataforma']
            
            sql = """
            INSERT INTO tb_telemetria_ia 
            (dispositivo_id, protocolo_nome, latitude, longitude, velocidade, ignicao, alerta_status, anatomia_string, payload_bruto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cur.execute(sql, (
                p.get('id'),
                analise['metadata'].get('protocolo'),
                p.get('lat'),
                p.get('lng'),
                p.get('vel'),
                p.get('ign'),
                p.get('status'),
                Json(analise['anatomia']),
                raw_hex
            ))
            
            conn.commit()
            cur.close()
            conn.close()
            print(f">>> [SUCESSO] Dispositivo {p.get('id')} processado via {analise['metadata'].get('protocolo')}")
        except Exception as e:
            print(f"Erro no Banco: {e}")

# --- PONTO DE ENTRADA DO SISTEMA ---
if __name__ == "__main__":
    parser = ParserInteligenteIA()
    
    # Exemplo: String de localização do protocolo GT06
    string_do_rastreador = "78781F120B081D112E1FCC0271D0A20668CB0001750D0A"
    
    print("Iniciando processamento metamórfico...")
    resultado_ia = parser.interpretar(string_do_rastreador)
    
    if resultado_ia:
        parser.salvar(string_do_rastreador, resultado_ia)