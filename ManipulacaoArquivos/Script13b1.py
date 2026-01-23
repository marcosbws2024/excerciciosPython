import os

# Esse comando descobre o caminho exato da pasta onde o seu script .py está
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_do_script, "dados13.txt")

try:
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        print(f"Lendo arquivo em: {caminho_arquivo}\n")
        for linha in arquivo:
            #print(f"Original: {repr(linha)}")
            print(f"Limpa:    {linha.strip()}")
            #print("-" * 20)
except FileNotFoundError:
    print(f"Erro: O arquivo 'dados13.txt' não foi encontrado na pasta {diretorio_do_script}")