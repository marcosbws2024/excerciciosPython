import sqlite3 as conector
import os

# 1. Caminho absoluto para não errar o arquivo do banco
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    # 2. Conexão e Cursor
    conexao = conector.connect(caminho_db)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # 3. UPDATE 1: Define óculos para todo mundo como True (1)
    comando1 = '''UPDATE Pessoa SET oculos = 1;'''
    cursor.execute(comando1)

    # 4. UPDATE 2: Usa marcador de posição (?)
    # No SQLite, False é guardado como 0
    comando2 = '''UPDATE Pessoa SET oculos = ? WHERE cpf = ?;'''
    cursor.execute(comando2, (0, 30000000099))

    # 5. UPDATE 3: Usa dicionário (nomeado) - Mais legível
    comando3 = '''UPDATE Pessoa SET oculos = :usa_oculos WHERE cpf = :cpf;'''
    cursor.execute(comando3, {"usa_oculos": 0, "cpf": 20000000099})

    # 6. Efetivação
    conexao.commit()
    print(f"Atualizações realizadas com sucesso! {cursor.rowcount} linhas afetadas.")

except conector.Error as e:
    print(f"Erro ao atualizar dados: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()