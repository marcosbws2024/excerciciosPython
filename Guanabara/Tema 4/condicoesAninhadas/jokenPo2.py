from random import randint
from time import sleep

# Configuração
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# Entrada do Jogador
try:
    jogador = int(input(""" Suas Opcoes
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura0

Opção Escolhida: """))

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)

    if jogador not in [0, 1, 2]:
        print("Opção inválida! Escolha 0, 1 ou 2.")
        exit()

except ValueError:
    print(" Entrada inválida! Digite apenas o número da opção.")
    exit()

# Saída das Escolhas
print('-' * 50)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-' * 50)

# --- ESTRUTURA CONDICIONAL (IFs) ---

# 1. Caso de Empate
if computador == jogador:
    print('🟰 EMPATE!')

# 2. Casos de Vitória do Computador
# Pedra (0) ganha de Tesoura (2)
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCEU!')
# Papel (1) ganha de Pedra (0)
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCEU!')
# Tesoura (2) ganha de Papel (1)
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCEU!')

# 3. Casos de Vitória do Jogador
# Se não foi empate nem vitória do computador, a vitória é do jogador.
else:
    print('🎉 JOGADOR VENCEU!')