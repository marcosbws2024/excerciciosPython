import sqlite3 as conector
import os
from BD_CONEXOES.modelo2 import Pessoa
# Verifique se o nome do arquivo está correto (JoinRecVeiculos.py)
from script19_4 import recuperar_veiculos

# 1. Localização do banco
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # 2. Busca as pessoas no banco
    cursor.execute("SELECT cpf, nome, nascimento, oculos FROM Pessoa;")
    reg_pessoas = cursor.fetchall()

    lista_final_pessoas = []
    
    for reg in reg_pessoas:
        pessoa = Pessoa(*reg)
        
        # AQUI ESTAVA O ERRO: Use sempre 'veiculos' sem acento
        # A função recuperar_veiculos deve retornar uma lista
        pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
        
        lista_final_pessoas.append(pessoa)

    # 3. Exibição formatada
    print(f"{'PROPRIETÁRIO':<20} | {'VEÍCULO (PLACA)'}")
    print("-" * 45)

    for p in lista_final_pessoas:
        # Se a lista de veiculos estiver vazia
        if not p.veiculos:
            print(f"{p.nome:<20} | (Sem veiculos)")
        else:
            for v in p.veiculos:
                # Verificamos se v.marca é um objeto ou apenas o ID
                marca_nome = v.marca.nome if hasattr(v.marca, 'nome') else str(v.marca)
                print(f"{p.nome:<20} | {v.placa} ({marca_nome})")

except NameError as e:
    print(f"❌ Erro de nome de variável: {e}")
    print("Dica: Verifique se você escreveu 'veiculos' com acento em algum lugar do código.")
except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()