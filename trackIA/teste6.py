import ollama
import json
import re
import psycopg2
from psycopg2.extras import Json

class MotorTelemetriaIA:
    def __init__(self):
        self.model = 'llama3.1'
        self.db_params = {
            "dbname": "RASTREAR",
            "user": "postgres",
            "password": "123",
            "host": "localhost"
        }

    def identificar_e_fatiar(self, raw_hex):
        """Identifica o protocolo e separa os dados dinamicamente."""
        # Lógica para GT06
        if raw_hex.startswith("7878"):
            return "GT06", {
                "header": raw_hex[0:4],
                "length": raw_hex[4:6],
                "protocol_id": raw_hex[6:8],
                "datetime": raw_hex[8:20],
                "lat_hex": raw_hex[22:30],
                "lng_hex": raw_hex[30:38],
                "speed_hex": raw_hex[38:40],
                "terminal_info": raw_hex[40:44]
            }
        
        # Espaço para adicionar outros protocolos (Suntech, Teltonika, etc) no futuro
        return "Desconhecido", {"raw": raw_hex}

    def processar_inteligencia(self, protocolo, fatias):
        """IA converte os pedaços separados em dados reais para a tabela."""
        prompt = f"""
        Como especialista em telemetria {protocolo}, converta estes campos HEX para Decimal:
        {json.dumps(fatias)}
        
        REGRAS:
        1. Converta lat_hex e lng_hex para float (Graus Decimais).
        2. Converta speed_hex para km/h.
        3. Analise terminal_info para definir ignicao (boolean) e alerta_status (texto).
        
        RETORNE APENAS JSON:
        {{"lat": 0.0, "lng": 0.0, "vel": 0.0, "ign": bool, "status": "string", "dev_id": "string"}}
        """
        
        try:
            response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
            res_json = re.search(r'\{.*\}', response['message']['content'], re.DOTALL).group()
            return json.loads(res_json)
        except:
            return None

    def inserir_banco(self, payload, protocolo, fatias, dados):
        """Preenche todas as colunas da tabela tb_telemetria_ia."""
        try:
            conn = psycopg2.connect(**self.db_params)
            cur = conn.cursor()
            
            sql = """
            INSERT INTO tb_telemetria_ia 
            (dispositivo_id, protocolo_nome, latitude, longitude, velocidade, ignicao, alerta_status, anatomia_string, payload_bruto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cur.execute(sql, (
                dados.get('dev_id', 'SEM_ID'),
                protocolo,
                dados.get('lat'),
                dados.get('lng'),
                dados.get('vel'),
                dados.get('ign'),
                dados.get('status'),
                Json(fatias), # Anatomia detalhada
                payload
            ))
            
            conn.commit()
            cur.close()
            conn.close()
            print(f">>> [OK] {protocolo} processado e salvo.")
        except Exception as e:
            print(f">>> [ERRO] Falha no banco: {e}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    motor = MotorTelemetriaIA()
    
    # Exemplo de Payload GT06
    payload_bruto = "78781F120B081D112E1FCC0271D0A20668CB0001750D0A"
    
    # 1. Separação dinâmica
    nome_proto, mapa_fatias = motor.identificar_e_fatiar(payload_bruto)
    
    if nome_proto != "Desconhecido":
        # 2. Conversão inteligente
        info_ia = motor.processar_inteligencia(nome_proto, mapa_fatias)
        
        if info_ia:
            # 3. Preenchimento da tabela
            motor.inserir_banco(payload_bruto, nome_proto, mapa_fatias, info_ia)