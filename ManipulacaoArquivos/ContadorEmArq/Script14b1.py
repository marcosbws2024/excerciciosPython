import os

# 1. Encontra o caminho da pasta onde este script está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))

# 2. Junta essa pasta com o nome do arquivo para criar o caminho relativo real
caminho_completo = os.path.join(diretorio_do_script, "dados13.txt")

try:
    with open(caminho_completo, "r", encoding="utf-8") as arquivo:
        print("Total REAL de linhas no arquivo: ")
        contador = 0
        for linha in arquivo:
            if linha.strip():
                contador += 1
        
        print(f"Total Real = {contador}")

except FileNotFoundError:
    print(f"Erro: O arquivo 'dados13.txt' não foi encontrado na pasta:")
    print(diretorio_do_script)