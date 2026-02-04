import sqlite3 as conector
import os
from BD_CONEXOES.modelo import Pessoa

# 1. Registro de conversores (DEVE vir antes da conexão)
def conv_bool(dado):
    # O SQLite entrega bytes ou int no conversor; tratamos ambos
    if isinstance(dado, bytes):
        dado = dado.decode()
    return True if str(dado) == '1' else False

# Registra para que colunas do tipo "BOOLEAN" sejam convertidas automaticamente
conector.register_converter("BOOLEAN", conv_bool)

# 2. Caminho dinâmico do banco
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(diretorio_do_script, "meu_banco.db")

conexao = None

try:
    # 3. Abertura com detecção de tipos declarados
    conexao = conector.connect(caminho_db, detect_types=conector.PARSE_DECLTYPES)
    cursor = conexao.cursor()

    # 4. Busca explícita (melhor prática para garantir a ordem das colunas)
    comando = '''SELECT cpf, nome, nascimento, oculos FROM Pessoa WHERE oculos = :usa_oculos;'''
    cursor.execute(comando, {"usa_oculos": 1})

    registros = cursor.fetchall()
    
    print(f"--- Relatório de Dados e Tipos ({len(registros)} encontrados) ---")
    
    for registro in registros:
        # Criamos o objeto desempacotando a tupla do banco
        pessoa = Pessoa(*registro)
        
        # Exibição detalhada com tipos (conforme seu pedido)
        # Ajustado para usar 'data_nascimento' e 'usa_oculos' (nomes comuns em classes modelo)
        print(f"\nCPF: {pessoa.cpf} | Tipo: {type(pessoa.cpf).__name__}")
        print(f"Nome: {pessoa.nome} | Tipo: {type(pessoa.nome).__name__}")
        
        # Tratamento de erro caso o atributo no modelo.py seja diferente
        try:
            print(f"Nascimento: {pessoa.data_nascimento} | Tipo: {type(pessoa.data_nascimento).__name__}")
        except AttributeError:
            print(f"Nascimento (via .nascimento): {pessoa.nascimento} | Tipo: {type(pessoa.nascimento).__name__}")
            
        try:
            print(f"Óculos: {pessoa.usa_oculos} | Tipo: {type(pessoa.usa_oculos).__name__}")
        except AttributeError:
            print(f"Óculos (via .oculos): {pessoa.oculos} | Tipo: {type(pessoa.oculos).__name__}")
            
        print("-" * 50)

except conector.Error as e:
    print(f"❌ Erro no banco: {e}")
except Exception as e:
    print(f"❌ Erro de sistema: {e}")

finally:
    if conexao:
        cursor.close()
        conexao.close()