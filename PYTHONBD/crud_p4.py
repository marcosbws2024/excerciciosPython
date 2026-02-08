import psycopg2

try:
    # Conexão com o banco
    conn = psycopg2.connect(
        database="TESTE_ESTACIO", 
        user="postgres", 
        password="123", 
        host="127.0.0.1", 
        port="5432"
    )
    
    # Mantendo a correção para caracteres especiais (ç, acentos, etc.)
    conn.set_client_encoding('LATIN1') 
    
    cur = conn.cursor()
    print("Conexão aberta com sucesso!")

    id_para_deletar = 1
    
    # Executando a exclusão de forma parametrizada (mais seguro)
    cur.execute('DELETE FROM public."AGENDA" WHERE "id" = %s', (id_para_deletar,))
    
    # O commit é obrigatório para tornar a exclusão permanente
    conn.commit()

    # Feedback baseado no número de linhas afetadas
    if cur.rowcount > 0:
        print(f"Sucesso: {cur.rowcount} registro(s) excluído(s).")
    else:
        print("Aviso: Nenhum registro encontrado com o ID informado.")

except Exception as e:
    print(f"Erro ao realizar a exclusão: {e}")

finally:
    # Garante o fechamento da conexão mesmo se houver erro
    if 'conn' in locals():
        conn.close()
        print("Conexão fechada.")