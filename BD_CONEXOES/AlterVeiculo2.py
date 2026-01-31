import sqlite3 as conector
import os

# 1. Localiza a pasta do script
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

try:
    # 2. Conexão
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 3. Comando para adicionar a coluna
    comando = '''ALTER TABLE Veiculo ADD COLUMN motor REAL;'''
    
    cursor.execute(comando)
    conexao.commit()
    print("Coluna 'motor' adicionada com sucesso!")

except conector.OperationalError:
    # Se a coluna já existir, o SQLite lança um OperationalError
    print("Aviso: A coluna 'motor' já existe na tabela Veiculo.")

except conector.Error as erro:
    print(f"Erro inesperado: {erro}")

finally:
    if conexao:
        cursor.close()
        conexao.close()