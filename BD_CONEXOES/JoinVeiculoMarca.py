import sqlite3
from BD_CONEXOES.modelo2 import Veiculo, Marca

def recuperar_veiculos(conexao, cpf):
    # 1. Aquisição de cursor
    cursor = conexao.cursor()

    # 2. Comando SQL com JOIN explícito
    # É melhor listar as colunas para evitar confusão com os índices
    comando = '''SELECT Veiculo.*, Marca.id, Marca.nome, Marca.sigla 
                 FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    
    cursor.execute(comando, (cpf,))

    # 3. Processamento dos registros
    veiculos = [] 
    registros = cursor.fetchall()
    
    for registro in registros:
        # A tabela Veiculo tem 6 colunas (0 a 5)
        # A tabela Marca começa a partir do índice 6
        
        # Criamos o objeto Marca (id, nome, sigla)
        marca = Marca(registro[6], registro[7], registro[8])
        
        # Criamos o objeto Veiculo e passamos o objeto marca no final
        veiculo = Veiculo(registro[0], registro[1], registro[2], registro[3], registro[4], marca)
        veiculos.append(veiculo)

    # 4. Fechamento seguro do cursor
    cursor.close()
    
    return veiculos
