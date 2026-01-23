import os

# 1. Garante que o Python encontre o arquivo na mesma pasta do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_relativo = os.path.join(diretorio_atual, "dados13.txt")

try:
    with open(caminho_relativo, "r", encoding="utf-8") as arquivo:
        contador = 0
        
        for linha in arquivo:
                contador += 1
        
        print(f"Total de linhas preenchidas no arquivo: {contador}")

except FileNotFoundError:
    print(f"Erro: O arquivo 'dados13.txt' não foi encontrado em: {diretorio_atual}")