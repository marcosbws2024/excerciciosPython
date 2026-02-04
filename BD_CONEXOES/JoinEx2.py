import sqlite3 as conector
import os
from modelo import Veiculo

# 1. Localização dinâmica do banco (mais seguro que "./")
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio, "meu_banco.db")

try:
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 2. Definição do comando com JOIN
    # Buscamos as colunas do Veículo e o NOME da Marca por último
    comando = ''' 
    SELECT v.placa, v.ano, v.cor, v.motor, v.proprietario, m.nome 
    FROM Veiculo v 
    JOIN Marca m ON m.id = v.marca;'''
    
    cursor.execute(comando)

    # 3. Recuperação e Instanciação
    reg_veiculos = cursor.fetchall()
    
    print(f"{'PLACA':<10} | {'MARCA'}")
    print("-" * 25)

    for reg_veiculo in reg_veiculos:
        # O *reg_veiculo desempacota os 6 valores do SELECT nos parâmetros da classe
        veiculo = Veiculo(*reg_veiculo)
        
        # O print abaixo usa os atributos do objeto criado
        print(f"{veiculo.placa:<10} | {veiculo.marca}")

except conector.Error as e:
    print(f"Erro no SQLite: {e}")

finally:
    # 4. Fechamento garantido (mesmo se ocorrer erro)
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()