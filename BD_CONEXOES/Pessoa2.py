import sqlite3 as conector
import os

# 1. Descobre o caminho da pasta onde o script está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None # Inicializa para evitar erro no finally caso a conexão falhe

try:
    # 2. Abertura de conexão usando o caminho dinâmico
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 3. Execução do comando (com IF NOT EXISTS para evitar erro de tabela já existente)
    comando = '''CREATE TABLE IF NOT EXISTS Pessoa (cpf INTEGER NOT NULL,
nome TEXT NOT NULL,nascimento DATE NOT NULL,oculos BOOLEAN NOT NULL,PRIMARY KEY (cpf));'''

    cursor.execute(comando)
 
    # 4. Efetivação do comando
    conexao.commit()
    print(f"Tabela 'Pessoa' verificada/criada com sucesso em: {caminho_db}")

except conector.DatabaseError as err:
    print("Erro de banco de dados:", err)

finally:
    # 5. Fechamento seguro das conexões
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")