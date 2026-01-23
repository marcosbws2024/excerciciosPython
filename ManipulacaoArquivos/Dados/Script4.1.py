import os

# Pega o diretório onde o script atual está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_script, "dados.txt")

with open(caminho_completo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(repr(conteudo))