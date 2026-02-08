import psycopg2

try:
    conn = psycopg2.connect(
        database="TESTE_ESTACIO", 
        user="postgres", 
        password="123", 
        host="127.0.0.1", 
        port="5432"
    )
    
    # --- SOLUÇÃO AQUI ---
    # Isso avisa ao Python como interpretar os caracteres especiais vindo do banco
    conn.set_client_encoding('LATIN1') 
    # --------------------

    cur = conn.cursor()
    print("Conexão aberta com sucesso!")

    id_busca = 1
    cur.execute('SELECT id, nome, telefone FROM public."AGENDA" WHERE id = %s', (id_busca,))
    
    registro = cur.fetchone()

    if registro:
        print(f"ID: {registro[0]}")
        print(f"Nome: {registro[1]}")
        print(f"Telefone: {registro[2]}")
    else:
        print("Nenhum registro encontrado.")

except Exception as e:
    print(f"Erro ao consultar o banco: {e}")

finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()