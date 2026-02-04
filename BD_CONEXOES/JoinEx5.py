import sqlite3 as conector
import os
from modelo import Pessoa
from JoinRecVeiculos import recuperar_veiculos

# 1. Ajuste de Caminho (Resolve o erro 'no such table')
# Isso descobre a pasta onde este arquivo .py está e aponta para o .db nela
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "meu_banco.db")

if not os.path.exists(caminho_banco):
    print(f"ERRO: O arquivo de banco de dados não foi encontrado em:\n{caminho_banco}")
else:
    try:
        # 2. Conexão
        conexao = conector.connect(caminho_banco)
        cursor = conexao.cursor()

        # 3. Execução do comando (Listando colunas para evitar erros de ordem)
        # Verifique se os nomes das colunas (cpf, nome...) batem com seu banco
        comando = '''SELECT cpf, nome, nascimento, oculos FROM Pessoa;'''
        cursor.execute(comando)

        pessoas = []
        reg_pessoas = cursor.fetchall()

        # 4. Processamento dos registros
        for reg_pessoa in reg_pessoas:
            # Cria o objeto Pessoa desempacotando a tupla reg_pessoa
            pessoa = Pessoa(*reg_pessoa)
            
            # Busca os veiculos usando a função que você importou
            # Passamos a conexão aberta e o CPF da pessoa
            pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
            
            pessoas.append(pessoa)

        # 5. Exibição dos dados na tela
        print(f"\n{' RELATÓRIO DE PROPRIETÁRIOS ':=^50}")
        
        if not pessoas:
            print("Nenhum registro de pessoa encontrado.")
        
        for pessoa in pessoas:
            print(f"\nProprietário: {pessoa.nome.upper()} (CPF: {pessoa.cpf})")
            
            if not pessoa.veiculos:
                print('\t[!] Nenhum veículo cadastrado para esta pessoa.')
            else:
                for v in pessoa.veiculos:
                    # v.marca.nome assume que v.marca é um objeto da classe Marca
                    print(f'\t> Veículo: {v.placa:<8} | Marca: {v.marca.nome}')
        
        print(f"\n{'='*50}")

    except conector.Error as erro:
        print(f"Erro no Banco de Dados: {erro}")
    
    finally:
        # 6. Fechamento seguro
        if 'conexao' in locals():
            cursor.close()
            conexao.close()
            print("\nConexão com o banco encerrada com segurança.")