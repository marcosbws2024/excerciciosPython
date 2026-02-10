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
        # Adicionei o encoding para evitar erros com nomes brasileiros do Faker
        self.conexao.set_client_encoding('LATIN1')
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

    # --- MÉTODO QUE ESTAVA FALTANDO ---
    def selecionar_dados(self):
        try:
            self.cursor.execute("SELECT id, titulo, autor, ano_publicacao, genero FROM livros")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao selecionar dados: {e}")
            return []

# O trecho abaixo popula o banco apenas se rodar este arquivo diretamente
if __name__ == "__main__":
    fake = Faker() 
    bd = BancoDados() 
    bd.criar_tabela() 
    print("Gerando dados fictícios...")
    for _ in range(10): # Reduzi para 10 apenas para teste rápido
        bd.inserir_dados(fake.catch_phrase(), fake.name(), fake.year(), fake.word())
    print("Dados inseridos com sucesso!")