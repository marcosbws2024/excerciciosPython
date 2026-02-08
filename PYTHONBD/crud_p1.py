import psycopg2

try:
    # O bloco 'with' garante que a conexão feche ao final do código
    with psycopg2.connect(
        database="TESTE_ESTACIO", 
        user="postgres", 
        password="123", # Removi o espaço extra que notei no seu código
        host="127.0.0.1", 
        port="5432"
    ) as conn:
        
        print("Conexão aberta com sucesso!")
        
        with conn.cursor() as cur:
            # Usamos %s como placeholders para os dados
            comando_sql = 'INSERT INTO public."AGENDA" (id, nome, telefone) VALUES (%s, %s, %s)'
            dados = (2, 'Pessoa 2', '02188888888')
            
            cur.execute(comando_sql, dados)
            print("Inserção realizada com sucesso!")
            
        # O commit acontece automaticamente ao sair do bloco 'with conn' 
        # se não houver erros.

except Exception as e:
    print(f"Erro ao conectar ou inserir: {e}")