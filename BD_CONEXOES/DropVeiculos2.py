import sqlite3 as conector
import os

# 1. Localiza a pasta do script para o caminho relativo funcionar sempre
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

try:
    # 2. Conexão e Ativação de Foreign Keys
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 3. DROP TABLE com segurança (IF EXISTS)
    # Isso evita que o código quebre se a tabela não existir
    comando1 = '''DROP TABLE IF EXISTS Veiculo;'''
    cursor.execute(comando1)

    # 4. CREATE TABLE com a nova coluna 'motor'
    comando2 = '''CREATE TABLE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''
    cursor.execute(comando2)

    # 5. Efetivação
    conexao.commit()
    print("Tabela Veiculo reiniciada com sucesso (incluindo coluna motor)!")

except conector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    if conexao:
        cursor.close()
        conexao.close()