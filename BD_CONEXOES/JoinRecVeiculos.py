from modelo import Veiculo, Marca

def recuperar_veiculos(conexao, cpf):
    # 1. Aquisição de cursor
    cursor = conexao.cursor()

    # 2. Comando SQL
    comando = '''SELECT * FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    
    try:
        cursor.execute(comando, (cpf,))

        # 3. Processamento dos registros
        veiculos = [] # Variável definida SEM acento
        registros = cursor.fetchall()
        
        for registro in registros:
            # A tabela Veiculo tem colunas 0 a 5. Marca começa no índice 6.
            marca = Marca(*registro[6:])
            veiculo = Veiculo(*registro[:5], marca)
            veiculos.append(veiculo)
            
    finally:
        # 4. Fechamento seguro do cursor
        cursor.close()
    
    # CORREÇÃO: Removido o acento para coincidir com a variável criada acima
    return veiculos