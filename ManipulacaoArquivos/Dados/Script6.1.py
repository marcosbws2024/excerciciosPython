import os

# 1. Garantir que o Python olhe para a pasta onde o script está salvo
# Isso resolve o erro de 'FileNotFoundError'
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 2. Abrir o arquivo (ajustei para 'exemplo.txt' conforme seu pedido)
arquivo = open("dados.txt", "r", encoding="utf-8")

# 3. CORREÇÃO: O nome correto do método é .readlines()
conteudo = arquivo.readlines()

print("Tipo de Conteúdo:", type(conteudo))
print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()