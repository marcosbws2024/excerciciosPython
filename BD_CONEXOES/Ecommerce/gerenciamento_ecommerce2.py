import sqlite3
import os

def conectar_banco(nome_banco):
    # Garante que o banco seja criado na mesma pasta do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(diretorio_atual, nome_banco)
    
    conexao = sqlite3.connect(caminho_completo)
    # Ativa as chaves estrangeiras para validar as relações entre tabelas
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      preco REAL NOT NULL,
                      estoque INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      cliente_id INTEGER NOT NULL,
                      produto_id INTEGER NOT NULL,
                      quantidade INTEGER NOT NULL,
                      data_pedido TEXT NOT NULL,
                      FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                      FOREIGN KEY (produto_id) REFERENCES Produtos(id))''')
    
    conexao.commit()
    print("Tabelas criadas com sucesso!")

def inserir_dados(conexao):
    cursor = conexao.cursor()
   
    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
   
    clientes = [('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')]
   
    # Ordem: cliente_id, produto_id, quantidade, data_pedido
    pedidos = [(1, 1, 2, '2023-06-15'),
               (2, 2, 1, '2023-06-16'),
               (3, 3, 3, '2023-06-17')]
   
    # Usamos INSERT OR IGNORE ou apenas INSERT se o banco for novo
    cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)', clientes)
    cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)', pedidos)
   
    conexao.commit()
    print("Dados inseridos com sucesso!")

# O bloco principal deve estar fora de qualquer função (coluna 0)
if __name__ == '__main__':
    minha_conexao = conectar_banco('ecommerce.db')
    try:
        criar_tabelas(minha_conexao)
        inserir_dados(minha_conexao)
    finally:
        minha_conexao.close()
        print("Conexão fechada.")