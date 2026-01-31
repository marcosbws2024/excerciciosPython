import sqlite3 as conector
import os

# 1. Define o caminho relativo dinâmico (mesma pasta do script)
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

# 2. Abertura de conexão e aquisição de cursor
conexao = conector.connect(caminho_db)
cursor = conexao.cursor()

# 3. Comando SQL
# Adicionei "IF NOT EXISTS" para o código não dar erro se você rodar ele duas vezes
comando = """CREATE TABLE IF NOT EXISTS Marca (id INTEGER NOT NULL,
nome TEXT NOT NULL,sigla CHARACTER(2) NOT NULL,PRIMARY KEY (id));"""

try:
    # 4. Execução do comando
    cursor.execute(comando)

    # 5. Efetivação do comando
    conexao.commit()
    print("Banco de dados e tabela preparados com sucesso!")
    print(f"Arquivo salvo em: {caminho_db}")

except conector.Error as erro:
    print(f"Erro no SQLite: {erro}")

finally:
    # 6. Fechamento das conexões (Sempre importante!)
    cursor.close()
    conexao.close()
