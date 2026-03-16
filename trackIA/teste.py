import ollama
import psycopg2
import json
from psycopg2.extras import Json

# --- CONFIGURAÇÃO DO BANCO ---
def salvar_no_banco(dados_finais, anatomia, raw_hex):
    try:
        conn = psycopg2.connect(
            dbname="RASTREAR", user="postgres", password="123", host="localhost"
        )
        cur = conn.cursor()
        
        sql = """
        INSERT INTO posicoes_rastreador 
        (imei, protocolo, latitude, longitude, velocidade, ignicao, status_sistema, decomposicao_tecnica, string_bruta)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        cur.execute(sql, (
            dados_finais.get('imei'),
            dados_finais.get('protocolo'),
            dados_finais.get('lat'),
            dados_finais.get('lng'),
            dados_finais.get('velocidade'),
            dados_finais.get('ignicao'),
            dados_finais.get('status'),
            Json(anatomia),
            raw_hex
        ))
        
        conn.commit()
        cur.close()
        conn.close()
        print(">>> Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")

# --- PARSER COM IA (LLAMA 3.1) ---
def parser_inteligente(string_hex):
    # Ensinando a lógica de documentação para a IA
    prompt_sistema = """
    Você é um especialista em protocolos de telemetria. Analise a string HEX e:
    1. Identifique o tamanho e o fabricante (GT06, Suntech, etc).
    2. Explique o significado de cada segmento (Fatiamento/Slicing).
    3. Converta valores brutos para dados legíveis (Lat/Lng em graus, Km/h, On/Off).
    
    Retorne APENAS um JSON com duas chaves:
    'anatomia': { 'segmento': 'significado' }
    'dados_finais': { 'imei', 'protocolo', 'lat', 'lng', 'velocidade', 'ignicao', 'status' }
    """

    try:
        response = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': prompt_sistema},
                {'role': 'user', 'content': f"Analise esta string: {string_hex}"}
            ]
        )
        
        # Processando a resposta da IA
        res_text = response['message']['content']
        dados = json.loads(res_text[res_text.find("{"):res_text.rfind("}")+1])
        
        return dados['dados_finais'], dados['anatomia']
    except Exception as e:
        print(f"Erro na IA: {e}")
        return None, None

# --- EXECUÇÃO ---
string_bruta = "78780D010358243001000001000D0A" # Exemplo GT06
print(f"Processando string: {string_bruta}")

dados_finais, anatomia = parser_inteligente(string_bruta)

if dados_finais:
    salvar_no_banco(dados_finais, anatomia, string_bruta)