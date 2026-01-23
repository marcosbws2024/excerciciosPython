import os

arquivo = open("dados.txt", "r", encoding="utf-8")
conteudo = arquivo.read()

print("Tipo de Conteúdo:" , type(conteudo))
print("Conteúdo retornado pelo read:")
print(repr(conteudo))
arquivo.close()