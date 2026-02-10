
import psycopg2 
from faker import Faker 
 
class BancoDados: 
       def __init__(self): 
           self.conexao = psycopg2.connect( 
               dbname="TESTE_ESTACIO", 
               user="postgres", 
               password="123", 
               host="localhost" 
           ) 
           self.cursor = self.conexao.cursor() 
        
       def criar_tabela(self): 
           self.cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS livros ( 
                   id SERIAL PRIMARY KEY, 
                   titulo VARCHAR(255), 
                   autor VARCHAR(255), 
                   ano_publicacao INTEGER, 
                   genero VARCHAR(100) 
               ) 
           """) 
           self.conexao.commit() 
 
       def inserir_dados(self, titulo, autor, ano_publicacao, genero): 
           self.cursor.execute(""" 
               INSERT INTO livros (titulo, autor, ano_publicacao, genero) 
               VALUES (%s, %s, %s, %s) 
           """, (titulo, autor, ano_publicacao, genero)) 
           self.conexao.commit() 
  

fake = Faker() 
bd = BancoDados() 
bd.criar_tabela() 
for _ in range(100): 
    bd.inserir_dados(fake.text(max_nb_chars=20), fake.name(), fake.year(), fake.word()) 
   