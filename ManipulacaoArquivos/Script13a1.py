import os

# 1. Ajusta o caminho para a pasta onde o script está
# Isso garante que ele ache o "dados13a.txt" se ele estiver na mesma pasta que o .py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 2. Adicionei o encoding="utf-8" para evitar erros com acentos e 'ç'
with open("dados13.txt", "r", encoding="utf-8") as arquivo:
    print("Representacao Original da Linha: ")
    for linha in arquivo:
        # O repr() mostra os caracteres "invisíveis", como o \n (quebra de linha)
        print(repr(linha))