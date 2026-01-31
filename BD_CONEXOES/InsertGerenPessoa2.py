import sqlite3 as conector
import os

# 1. Caminho absoluto dinâmico
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

# Converter o caminho para o formato URI (necessário para usar o modo 'rw' sem criar arquivo)
caminho_uri = f"file:{caminho_db}?mode=rw"

conexao = None

try:
    # 2. Conexão no modo 'rw' (read/write). 
    # Se o arquivo não existir, o sqlite3.OperationalError será disparado aqui.
    conexao = conector.connect(caminho_uri, uri=True)
    cursor = conexao.cursor()

    # 3. Comando de Inserção (Sem criar tabela, apenas inserindo)
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                 VALUES (12345678900, 'João', '2000-01-31', 1);'''
    
    cursor.execute(comando)
    conexao.commit()
    
    if cursor.rowcount > 0:
        print("✅ Dados inseridos com sucesso!")
    else:
        print("⚠️ Aviso: Pessoa não inserida (CPF já cadastrado).")

except conector.OperationalError as e:
    if "unable to open database file" in str(e):
        print(f"❌ ERRO: O arquivo '{caminho_db}' não existe fisicamente na pasta.")
    elif "no such table" in str(e):
        print("❌ ERRO: O banco existe, mas a tabela 'Pessoa' não foi criada nele.")
    else:
        print(f"❌ Erro Operacional: {e}")

except conector.Error as erro:
    print(f"❌ Erro de Banco de Dados: {erro}")

finally:
    if conexao:
        cursor.close()
        conexao.close()