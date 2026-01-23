import os

# Pega o caminho da pasta onde o seu script .py está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))

# Une a pasta do script com o nome do arquivo txt
caminho_relativo = os.path.join(diretorio_do_script, "dados13.txt")

try:
    with open(caminho_relativo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
        # Conta as ocorrências da palavra "Olá"
        contador = texto.count("Olá")
        print(f"Total de 'Olás' encontrados = {contador}")

except FileNotFoundError:
    print(f"Erro: O arquivo 'dados13.txt' não foi encontrado na pasta: {diretorio_do_script}")