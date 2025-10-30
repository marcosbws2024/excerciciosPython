cidade = input("Nome da cidade: ")

# 1. Limpa espaços laterais (.strip()) e transforma em minúsculas (.lower())
cidade_formatada = cidade.strip().lower()

# 2. Verifica se a string formatada começa com "santo"
if cidade_formatada.startswith("santo"):
    print('A cidade começa com Santo')
else:
    print('A cidade NÃO começa com Santo')

# segunda solucao
if cidade_formatada.find("santo") == 0:
    print('A Cidade começa com Santo')
else:
    print('A Cidade não começa com Santo')