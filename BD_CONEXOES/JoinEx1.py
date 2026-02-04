import sqlite3 as conector
import os
from modelo import Veiculo

# 1. Caminho absoluto (evita erro de arquivo não encontrado)
caminho_db = os.path.join(os.path.dirname(__file__), "meu_banco.db")

try:
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 2. SELECIONE AS COLUNAS EXPLICITAMENTE
    # Isso garante que a ordem sempre coincida com o seu objeto Veiculo
    comando = '''SELECT placa, ano, cor, motor, proprietario, marca FROM Veiculo;'''
    cursor.execute(comando)

    reg_veiculos = cursor.fetchall()
    
    for reg in reg_veiculos:
        # Desempacota os valores na classe Veiculo
        veiculo = Veiculo(*reg)
        print(f"Placa: {veiculo.placa}, Marca: {veiculo.marca}")

except conector.Error as e:
    print(f"Erro no banco de dados: {e}")

finally:
    # 3. Fechamento seguro
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()