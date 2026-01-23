import os

# 1. Descobre a pasta onde este script (Script4.py) está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# 2. Une essa pasta ao nome do arquivo 'dados.txt'
caminho_completo = os.path.join(diretorio_atual, "dados.txt")

# 3. Abre usando o caminho completo (o resto do seu código continua igual)
arquivo = open(caminho_completo, "r", encoding="utf-8")

conteudo = arquivo.readline()
print("Tipo de Conteúdo:", type(conteudo))
print("Conteúdo retornado pelo readline:")      
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Proximo conteúdo retornado:")
print(repr(proximo_conteudo))

arquivo.close()