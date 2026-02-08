import psycopg2

try:
    # Conexão (Removido o espaço de " postgres")
    conn = psycopg2.connect(
        database="TESTE_ESTACIO", 
        user="postgres", 
        password="123", 
        host="127.0.0.1", 
        port="5432"
    )
    
    # Define a codificação para evitar o erro de 'utf-8' codec
    conn.set_client_encoding('LATIN1') 
    
    cur = conn.cursor()
    print("Conexão com o Banco de Dados aberta com sucesso!")

    # 1. Consulta antes da atualização
    print("\n--- Consulta antes da atualização ---")
    cur.execute('SELECT * FROM public."AGENDA" WHERE id = 1')
    print(cur.fetchone())

    # 2. Atualização do registro
    # Usar %s é mais seguro e evita erros com strings
    novo_telefone = '02188888888'
    id_alvo = 1
    
    cur.execute('UPDATE public."AGENDA" SET "telefone" = %s WHERE "id" = %s', (novo_telefone, id_alvo))
    conn.commit()
    print("Registro Atualizado com sucesso!")

    # 3. Consulta depois da atualização
    print("\n--- Consulta depois da atualização ---")
    cur.execute('SELECT * FROM public."AGENDA" WHERE id = 1')
    print(cur.fetchone())

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("\nConexão fechada.")