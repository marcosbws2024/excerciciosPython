import sqlite3 as conector
import os
from modelo import Marca, Veiculo

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    conexao = conector.connect(caminho_db)
    # ATENÇÃO: Isso obriga que o proprietário e a marca existam!
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # 1. GARANTIR QUE AS PESSOAS EXISTAM (Obrigatório para a FK de Veiculo)
    # Se esses CPFs não existirem, o Veiculo não entra.
    comando_pessoa = "INSERT OR IGNORE INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)"
    pessoas = [
        (10000000099, 'Dono A', '1990-01-01', 0),
        (20000000099, 'Dono B', '1985-05-12', 1),
        (30000000099, 'Dono C', '1992-10-20', 0)
    ]
    cursor.executemany(comando_pessoa, pessoas)

    # 2. INSERIR MARCAS
    comando_marca = '''INSERT OR IGNORE INTO Marca (id, nome, sigla) VALUES (:id, :nome, :sigla);'''
    marca1 = Marca(1, "Marca A", "MA")
    marca2 = Marca(2, "Marca B", "MB")
    cursor.execute(comando_marca, vars(marca1))
    cursor.execute(comando_marca, vars(marca2))

    # 3. INSERIR VEÍCULOS
    comando_veiculo = '''INSERT OR IGNORE INTO Veiculo (placa, ano, cor, motor, proprietario, marca)
                         VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    
    veiculos = [
        Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, 1),
        Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, 1),
        Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, 2),
        Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, 2)
    ]

    for v in veiculos:
        cursor.execute(comando_veiculo, vars(v))

    conexao.commit()
    print("✅ Sucesso: Pessoas, Marcas e Veículos processados!")

except conector.IntegrityError as e:
    print(f"❌ Erro de Integridade: {e}")
    print("DICA: Verifique se o ID da Marca ou o CPF do Proprietário estão corretos.")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")

finally:
    if conexao:
        conexao.close()