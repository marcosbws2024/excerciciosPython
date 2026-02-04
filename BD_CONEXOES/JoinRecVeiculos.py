import sqlite3 as conector
import os
from BD_CONEXOES.modelo2 import Veiculo

# 1. Caminho dinâmico (evita erro de "banco não encontrado")
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio, "meu_banco.db")

# 2. Abertura de conexão
conexao = conector.connect(caminho_db)
cursor = conexao.cursor()

# 3. Comando SQL
# Dica: Selecione exatamente as colunas na ordem que o __init__ do Veiculo espera
comando = ''' 
SELECT v.placa, v.ano, v.cor, v.motor, v.proprietario, m.nome 
FROM Veiculo v 
JOIN Marca m ON m.id = v.marca;'''

cursor.execute(comando)

# 4. Recuperação e Instanciação
reg_veiculos = cursor.fetchall()

print(f"{'PLACA':<10} | {'MARCA'}")
print("-" * 25)

for reg in reg_veiculos:
    # O '*' espalha os 6 valores do registro nos parâmetros do Veiculo
    veiculo = Veiculo(*reg) 
    
    # Se no seu modelo.py o atributo se chama 'marca', o print abaixo funciona:
    print(f"{veiculo.placa:<10} | {veiculo.marca}")

# 5. Fechamento seguro
cursor.close()
conexao.close()