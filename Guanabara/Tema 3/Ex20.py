frase = input("Digite uma frase: ")
frase = frase.upper().strip()

quantidadeLetraA = frase.count('A')
print(quantidadeLetraA)

primeira_posicao = frase.find('A')
ultima_posicao = frase.rfind('A')
print(f"A primeira letra 'A' está na posição: {primeira_posicao + 1} (Índice {primeira_posicao}).")
print(f"A última letra 'A' está na posição: {ultima_posicao + 1} (Índice {ultima_posicao}).")
