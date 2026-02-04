from modelo import Veiculo, Marca

def recuperar_veiculos(conexao, cpf):
    # 1. Aquisição de cursor
    cursor = conexao.cursor()

    # 2. Comando SQL com JOIN
    # Mantive o SELECT * que você usou, mas com o filtro de CPF
    comando = '''SELECT * FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    
    cursor.execute(comando, (cpf,))

    # 3. Processamento dos registros
    veiculos = [] # Variável consistente (sem acento)
    registros = cursor.fetchall()
    
    for registro in registros:
        # A tabela Veiculo tem 6 colunas (0 a 5)
        # A tabela Marca começa a partir do índice 6: id, nome, sigla
        
        # Criamos o objeto Marca com os dados do JOIN (colunas 6, 7 e 8)
        marca = Marca(*registro[6:])
        
        # Criamos o objeto Veiculo com as primeiras 5 colunas e passamos o objeto marca
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    # 4. Fechamento seguro do cursor
    cursor.close()
    
    # Retorno SEM acento para bater com a definição acima
    return veiculos