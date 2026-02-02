import sqlite3 as conector
import os
# Certifique-se de que o arquivo modelo.py existe na mesma pasta
from modelo import Marca, Veiculo

# 1. Localiza o banco na mesma pasta do script
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    # 2. Conexão e ativação de chaves estrangeiras
    conexao = conector.connect(caminho_db)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # 3. Inserção na tabela Marca (omitindo o ID para usar AUTOINCREMENT se configurado)
    # Se o ID não for automático, use (id, nome, sigla) e :id
    comando1 = '''INSERT OR IGNORE INTO Marca (id, nome, sigla) VALUES (:id, :nome, :sigla);'''

    marca1 = Marca(1, "Marca A", "MA")
    cursor.execute(comando1, vars(marca1))

    marca2 = Marca(2, "Marca B", "MB")
    cursor.execute(comando1, vars(marca2))

    # 4. Inserção na tabela Veiculo
    # Nota: A ordem dos atributos no objeto Veiculo deve ser igual às colunas
    comando2 = '''INSERT OR IGNORE INTO Veiculo (placa, ano, cor, motor, proprietario, marca)
                  VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''

    veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, 1)
    veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, 1)
    veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, 2)
    veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, 2)

    # Executando as inserções
    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    # 5. Efetivação
    conexao.commit()
    print("Marcas e Veículos processados com sucesso!")

except conector.IntegrityError as e:
    print(f"Erro de integridade (verifique se os donos/marcas existem): {e}")
except conector.Error as e:
    print(f"Erro no banco de dados: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()