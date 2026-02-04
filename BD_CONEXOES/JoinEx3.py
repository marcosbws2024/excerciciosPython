import sqlite3 as conector
import os
from modelo import Veiculo, Marca

# 1. Ajuste do Caminho: Garante que ele abra o banco na pasta correta
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_atual, "meu_banco.db")

conexao = conector.connect(caminho_db)
cursor = conexao.cursor()

# 2. Correção do SQL: Nome da tabela com "V" maiúsculo (conforme padrão anterior)
# Também é boa prática usar apelidos (v, m) para evitar confusão
comando = '''SELECT * FROM
             Veiculo JOIN Marca ON Marca.id = Veiculo.marca;'''

try:
    cursor.execute(comando)
    registros = cursor.fetchall()

    for registro in registros:
        # A lógica de fatiamento depende da ordem exata das colunas no banco
        # Veiculo (0 a 5) | Marca (6 a 8)
        marca = Marca(*registro[6:])
        
        # Passamos as primeiras 5 colunas e o objeto marca criado acima
        veiculo = Veiculo(*registro[:5], marca)
        
        print(f"Placa: {veiculo.placa}, Marca: {veiculo.marca.nome}")

except conector.OperationalError as e:
    print(f"❌ Erro de Banco de Dados: {e}")
    print("Dica: Verifique se o nome da tabela no banco é 'Veiculo' ou 'veiculo'.")

finally:
    # 3. Fechamento seguro
    cursor.close()
    conexao.close()