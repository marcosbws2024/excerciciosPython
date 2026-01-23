with open("dados13.txt", "r") as arquivo:
    print("Representacao Original da Linha: ")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha))