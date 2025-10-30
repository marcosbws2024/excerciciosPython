nomeCompleto = input("Digite seu nome: ")

# A variável nomeCompletoFormatado está ok para outras operações, mas não é usada no código abaixo.

# CORREÇÃO CRUCIAL:
# 1. Tira espaços laterais (.strip())
# 2. Divide a string em uma LISTA de palavras (nomes e sobrenomes) usando .split()
listaNomes = nomeCompleto.strip().split()

# Correção na verificação: verifica o tamanho da LISTA (quantos nomes foram digitados)
if len(listaNomes) > 0:

    # [0] pega o primeiro item da lista (o primeiro nome)
    primeiro_nome = listaNomes[0]

    # [-1] pega o último item da lista (o último nome/sobrenome)
    ultimo_nome = listaNomes[-1]

    print("=" * 30)
    print(f"Primeiro nome: {primeiro_nome.capitalize()}")
    print(f"Último nome: {ultimo_nome.capitalize()}")
    print("=" * 30)
else:
    print("Voce não digitou nenhum nome")