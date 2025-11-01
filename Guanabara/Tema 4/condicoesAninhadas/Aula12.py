nome = input("Qual se nome: ")

if nome == "Marcos":
    print("Que mome Bonito")
elif nome == "Maria" or nome == "Paulo" or nome == "Camila":
     print("seu nome é popular no brasil")
elif nome in "Carlito" or nome == "Teves":
    print("Eca! é fã de futebol Argentino ?")
else:
    print("Normal seu nome")
print("tenha um boa dia, {}!".format(nome))