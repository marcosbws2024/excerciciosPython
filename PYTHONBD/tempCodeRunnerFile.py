import psycopg2
conn = psycopg2.connect(database = "TESTE_ESTACIO", user="postgres" , password=" 123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 
conn.commit() 
print("Inserção realizada com sucesso!"); conn.close()