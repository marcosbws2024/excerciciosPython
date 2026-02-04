import sqlite3 as conector
import os
from modelo import Veiculo, Marca

# 1. Garante que o Python encontre o banco na mesma pasta do script
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio, "meu_banco.db")

try:
    conexao = conector.connect(caminho_db)
    # Row_factory permite acessar dados pelo nome da coluna: registro['placa']
    conexao.row_factory = conector.Row 
    cursor = conexao.cursor()

    # 2. SQL com nomes explícitos para evitar erros de índice
    comando = '''
        SELECT 
            v.placa, v.ano, v.cor, v.motor, v.proprietario,
            m.id AS marca_id, m.nome AS marca_nome, m.sigla AS marca_sigla
        FROM Veiculo v
        JOIN Marca m ON m.id = v.marca;
    '''
    cursor.execute(comando)
    registros = cursor.fetchall()

    # 3. Processamento dos objetos
    for reg in registros:
        # Criamos a Marca usando os nomes das colunas definidos no 'AS' do SQL
        marca = Marca(reg['marca_id'], reg['marca_nome'], reg['marca_sigla'])
        
        # Criamos o Veiculo injetando o objeto marca
        veiculo = Veiculo(
            reg['placa'], 
            reg['ano'], 
            reg['cor'], 
            reg['motor'], 
            reg['proprietario'], 
            marca
        )
        
        print(f"Placa: {veiculo.placa} | Marca: {veiculo.marca.nome} ({veiculo.marca.sigla})")

except conector.Error as e:
    print(f"Erro no banco de dados: {e}")

finally:
    # 4. Fechamento garantido
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()