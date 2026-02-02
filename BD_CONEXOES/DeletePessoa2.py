import sqlite3 as conector
import os

# 1. Localiza o banco na pasta correta
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    # 2. Conexão e ativação de restrições
    conexao = conector.connect(caminho_db)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # 3. Execução do DELETE
    # Dica: Usar parâmetros (?) é mais seguro contra SQL Injection
    cpf_para_excluir = 12345678900
    comando = '''DELETE FROM Pessoa WHERE cpf = ?;'''
    
    cursor.execute(comando, (cpf_para_excluir,))

    # 4. Efetivação
    conexao.commit()
    
    if cursor.rowcount > 0:
        print(f"✅ Pessoa com CPF {cpf_para_excluir} removida com sucesso!")
    else:
        print("⚠️ Aviso: Nenhum registro encontrado com esse CPF.")

except conector.IntegrityError as e:
    print(f"❌ Erro de Integridade: Não é possível excluir esta pessoa pois ela possui veículos cadastrados.")
    print(f"Detalhes: {e}")

except conector.Error as e:
    print(f"❌ Erro no SQLite: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()