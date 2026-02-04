import sqlite3
import os

# --- CLASSES DE MODELO ---
class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pedido:
    def __init__(self, cliente_id, livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido

# --- FUNÇÕES DE BANCO DE DATA ---

def conectar_banco(nome_banco):
    # Usa caminho absoluto para evitar erros de localização
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio, nome_banco)
    return sqlite3.connect(caminho)

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      titulo TEXT NOT NULL,
                      autor TEXT NOT NULL,
                      preco REAL NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      livro_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (livro_id) REFERENCES Livros(id))''')
    conexao.commit()

def inserir_dados(conexao):
    cursor = conexao.cursor()    

    # Verificação simples: só insere se as tabelas estiverem vazias
    cursor.execute('SELECT COUNT(*) FROM Livros')
    if cursor.fetchone()[0] == 0:
        livros = [Livro('Python para Iniciantes', 'John Doe', 39.99),
                  Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 49.99),
                  Livro('Inteligência Artificial', 'Alan Turing', 59.99)]    

        clientes = [Cliente('Alice', 'alice@example.com'),
                    Cliente('Bob', 'bob@example.com'),
                    Cliente('Charlie', 'charlie@example.com')]    

        pedidos = [Pedido(1, 1, 2, '2023-06-15'),
                   Pedido(2, 2, 1, '2023-06-16'),
                   Pedido(3, 3, 3, '2023-06-17')]    

        for livro in livros:
            cursor.execute('INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)', vars(livro))    
            
        for cliente in clientes:
            cursor.execute('INSERT INTO Clientes (nome, email) VALUES (:nome, :email)', vars(cliente))  
              
        for pedido in pedidos:
            cursor.execute('INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)', vars(pedido))    
        
        conexao.commit()
        print("Dados inseridos com sucesso!")
    else:
        print("O banco já possui dados, pulando inserção.")

def exibir_pedidos(conexao):
    cursor = conexao.cursor()   
    query = '''    
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''    
    cursor.execute(query)
    registros = cursor.fetchall()    
    
    print('\n--- LISTA DE PEDIDOS ---')
    print(f"{'ID':<3} | {'Cliente':<10} | {'Livro':<30} | {'Qtd':<3} | {'Data'}")
    print("-" * 70)

    for p in registros:        
        print(f"{p[0]:<3} | {p[1]:<10} | {p[2]:<30} | {p[3]:<3} | {p[4]}")

# --- EXECUÇÃO ---

if __name__ == '__main__':
    conexao_obj = conectar_banco('livraria.db')
    try:
        criar_tabelas(conexao_obj)
        inserir_dados(conexao_obj)
        exibir_pedidos(conexao_obj)
    finally:
        conexao_obj.close()