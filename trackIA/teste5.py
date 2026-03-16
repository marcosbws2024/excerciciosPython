import ollama
import json
import re
import psycopg2
from psycopg2.extras import Json

class TrackIAGenerator:
    def __init__(self):
        self.model = 'llama3.1'
        self.db_params = {
            "dbname": "RASTREAR",
            "user": "postgres",
            "password": "123",
            "host": "localhost"
        }

    def fatiar_gt06(self, raw_hex):
        """Separação cirúrgica dos campos do protocolo GT06."""
        if len(raw_hex) < 44: return None
        
        return {
            "header": raw_hex[0:4],
            "length": raw_hex[4:6],
            "protocol_id": raw_hex[6:8],
            "datetime_hex": raw_hex[8:20],
            "lat_hex": raw_hex[22:30],
            "lng_hex": raw_hex[30:38],
            "speed_hex": raw_hex[38:40],
            "status_hex": raw_hex[40:44]
        }

    def converter_com_ia(self, fatias):
        """Usa a IA para transformar HEX em dados decimais reais."""
        prompt = f"""
        Converta os campos HEX do protocolo GT06 abaixo para valores decimais:
        {json.dumps(fatias)}
        
        REGRAS:
        - lat_hex/lng_hex: Converta para float (Decimal Degrees).
        - speed_hex: Converta para float (km/h).
        - status_hex: Determine se a ignição é true ou false.
        
        Retorne APENAS um JSON com as chaves: lat, lng, vel, ign, status_desc.
        """
        try:
            response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
            json_match = re.search(r'\{.*\}', response['message']['content'], re.DOTALL)
            return json.loads(json_match.group()) if json_match else None
        except: return None

    def salvar_banco(self, raw_hex, fatias, dados_ia):
        """Guarda as informações na tabela tb_telemetria_ia."""
        try:
            conn = psycopg2.connect(**self.db_params)
            cur = conn.cursor()
            
            sql = """
            INSERT INTO tb_telemetria_ia 
            (dispositivo_id, protocolo_nome, latitude, longitude, velocidade, ignicao, alerta_status, anatomia_string, payload_bruto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Aqui definimos 'GT06' como o nome do protocolo
            valores = (
                "ID_GERADO_OU_EXTRAIDO", # Você pode extrair o ID do login packet depois
                "GT06", 
                dados_ia.get('lat'),
                dados_ia.get('lng'),
                dados_ia.get('vel'),
                dados_ia.get('ign'),
                dados_ia.get('status_desc'),
                Json(fatias), # Guarda o fatiamento técnico
                raw_hex
            )
            
            cur.execute(sql, valores)
            conn.commit()
            cur.close()
            conn.close()
            print(">>> [SUCESSO] Dados salvos no PostgreSQL (GT06).")
        except Exception as e:
            print(f">>> [ERRO] Banco de dados: {e}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    sistema = TrackIAGenerator()
    payload = "78781F120B081D112E1FCC0271D0A20668CB0001750D0A"
    
    print("Processando GT06...")
    fatias_tecnicas = sistema.fatiar_gt06(payload)
    
    if fatias_tecnicas:
        dados_convertidos = sistema.converter_com_ia(fatias_tecnicas)
        if dados_convertidos:
            sistema.salvar_banco(payload, fatias_tecnicas, dados_convertidos)