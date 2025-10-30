nome = input("Qual o seu nome completo: ")
nomeFormatado = nome.upper().strip()
nomeBusca = 'SILVA'

# CORREÇÃO: Verifica se o resultado NÃO É -1
if nomeFormatado.find(nomeBusca) != -1:
    print("Tem Silva")
else:
    print("Não Tem Silva")

if nomeBusca in nomeFormatado:
    print("Tem Silva")
else:
    print("Não Tem Silva")