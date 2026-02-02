import sqlite3 as conector
import os
from modelo import Pessoa

# 1. Localiza o banco
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    conexao = conector.connect(caminho_db)
    cursor = conexao.cursor()

    # Seleção explícita para garantir a ordem no objeto
    comando = '''SELECT cpf, nome, nascimento, oculos FROM Pessoa WHERE oculos = 1;'''
    cursor.execute(comando)

    registros = cursor.fetchall()
    
    print(f"Total de registros: {len(registros)}")
    print("-" * 50)

    for registro in registros:
        # Instancia o objeto (certifique-se que os nomes batem com o modelo.py)
        pessoa = Pessoa(*registro)
        
        # Exibindo dados e tipos
        print(f"CPF: {pessoa.cpf} | Tipo: ({type(pessoa.cpf).__name__})")
        print(f"Nome: {pessoa.nome} | Tipo: ({type(pessoa.nome).__name__})")
        
        # Ajustado para 'data_nascimento' e 'usa_oculos' conforme seu erro anterior
        print(f"Nascimento: {pessoa.data_nascimento} | Tipo: ({type(pessoa.data_nascimento).__name__})")
        print(f"Óculos: {pessoa.usa_oculos} | Tipo: ({type(pessoa.usa_oculos).__name__})")
        print("-" * 50)

except Exception as e:
    print(f"❌ Erro ao processar dados: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()