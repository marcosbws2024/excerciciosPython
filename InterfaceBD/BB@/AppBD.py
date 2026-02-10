import psycopg2 

class BancoDados: 
    def __init__(self): 
        # Mantendo sua conexão original
        self.conexao = psycopg2.connect( 
            dbname="TESTE_ESTACIO", 
            user="postgres", 
            password="123", 
            host="localhost" 
        ) 
        self.conexao.set_client_encoding('LATIN1') # Proteção contra erro de acentuação
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

    def selecionar_dados(self):
        self.cursor.execute("SELECT id, titulo, autor, ano_publicacao, genero FROM livros ORDER BY id")
        return self.cursor.fetchall()

    # --- NOVO MÉTODO: ATUALIZAR ---
    def atualizar_dado(self, id_livro, titulo, autor, ano, genero):
        try:
            sql = """ UPDATE livros 
                      SET titulo = %s, autor = %s, ano_publicacao = %s, genero = %s 
                      WHERE id = %s """
            self.cursor.execute(sql, (titulo, autor, ano, genero, id_livro))
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False

    # --- NOVO MÉTODO: DELETAR ---
    def deletar_dado(self, id_livro):
        try:
            self.cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()