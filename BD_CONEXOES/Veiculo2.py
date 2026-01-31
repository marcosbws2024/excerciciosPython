import sqlite3 as conector
import os

# 1. Localiza a pasta do script para o caminho relativo funcionar sempre
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

try:
    # 2. Conexão
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 3. ATIVAÇÃO DE CHAVES ESTRANGEIRAS
    # Por padrão, o SQLite ignora as FKs. Esse comando ativa a verificação.
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 4. Comando SQL (com IF NOT EXISTS)
    comando = '''CREATE TABLE IF NOT EXISTS Veiculo (
                  placa CHARACTER(7) NOT NULL,
                  ano INTEGER NOT NULL,
                  cor TEXT NOT NULL,
                  proprietario INTEGER NOT NULL,
                  marca INTEGER NOT NULL,
                  PRIMARY KEY (placa),
                  FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                  FOREIGN KEY(marca) REFERENCES Marca(id)
                  );'''

    cursor.execute(comando)
    conexao.commit()
    print("Tabela 'Veiculo' criada com sucesso!")

except conector.Error as erro:
    print(f"Erro ao criar tabela: {erro}")

finally:
    if conexao:
        cursor.close()
        conexao.close()