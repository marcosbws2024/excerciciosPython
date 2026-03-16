import ollama
import psycopg2
import json
from psycopg2.extras import Json

# --- 1. CONFIGURAÇÃO DE CONEXÃO ---
def conectar_banco():
    return psycopg2.connect(
        dbname="seu_banco",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

# --- 2. O CORAÇÃO DO PARSER (IA) ---
def parser_metamorfico(string_bruta):
    """
    Simula a leitura da documentação técnica para fatiar e entender a string.
    """
    # Este é o 'conhecimento' da documentação que passamos para o Llama
    instrucao_documentacao = """
    Você é um engenheiro de protocolos de rastreamento. Sua tarefa é:
    1. Analisar o tamanho total da string.
    2. Identificar o processador/firmware (Ex: GT06, Suntech, Coban).
    3. Separar (slice) a string conforme as regras de cada protocolo:
       - GT06: Header(2B), Length(1B), ProtocolID(1B), Data, Serial, Checksum.
       - Suntech: ASCII separado por ';', identificar cada campo pelo índice.
    4. Converter valores hexadecimais para decimais (considerando Little/Big Endian).
    5. Retornar APENAS um JSON com as chaves: 'identificacao', 'anatomia_string', 'valores_convertidos'.
    """

    try:
        response = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': instrucao_documentacao},
                {'role': 'user', 'content': f"Decomponha tecnicamente esta string: {string_bruta}"}
            ]
        )
        
        # Extrair apenas o conteúdo JSON da resposta da IA
        conteudo = response['message']['content']
        json_inicio = conteudo.find('{')
        json_fim = conteudo.rfind('}') + 1
        return json.loads(conteudo[json_inicio:json_fim])
    
    except Exception as e:
        print(f"Erro no processamento da IA: {e}")
        return None

# --- 3. INSERÇÃO NO POSTGRESQL ---
def salvar_no_sistema(raw_string, dados_decompostos):
    try:
        conn = conectar_banco()
        cur = conn.cursor()
        
        sql = """
        INSERT INTO log_rastreadores 
        (string_original, tamanho_string, protocolo_identificado, anatomia_json, dados_finais)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        cur.execute(sql, (
            raw_string,
            len(raw_string),
            dados_decompostos.get('identificacao'),
            Json(dados_decompostos.get('anatomia_string')),
            Json(dados_decompostos.get('valores_convertidos'))
        ))
        
        conn.commit()
        cur.close()
        conn.close()
        print(">>> String processada e mapeada no banco com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")

# --- 4. EXECUÇÃO ---
if __name__ == "__main__":
    # Exemplo de uma string que chegaria do seu servidor Socket
    exemplo_payload = "78780D010358243001000001000D0A"
    
    print("Iniciando análise metamórfica...")
    resultado = parser_metamorfico(exemplo_payload)
    
    if resultado:
        salvar_no_sistema(exemplo_payload, resultado)