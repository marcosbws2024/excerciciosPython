import random

# --- 1. CONFIGURAÇÃO ---
opcoes = ["PEDRA", "PAPEL", "TESOURA"]

print("--- JOGO JOKENPÔ (PEDRA, PAPEL E TESOURA) ---")
print("Regras: Pedra > Tesoura | Tesoura > Papel | Papel > Pedra")
print("-" * 50)

# --- 2. ENTRADA DO USUÁRIO ---
try:
    escolha_usuario_str = input("Escolha 1: PEDRA, 2: PAPEL ou 3: TESOURA? (Digite o número) ")
    escolha_usuario_int = int(escolha_usuario_str) - 1  # Converte a entrada (1, 2, 3) para índice (0, 1, 2)

    # Verifica se a entrada é válida
    if escolha_usuario_int not in [0, 1, 2]:
        print("❌ Opção inválida! Por favor, digite 1, 2 ou 3.")
        exit()

    escolha_usuario = opcoes[escolha_usuario_int]

except ValueError:
    print("❌ Entrada inválida! Digite apenas o número da opção.")
    exit()

# --- 3. ESCOLHA DO COMPUTADOR ---
escolha_computador = random.choice(opcoes)

print(f"\nVocê escolheu: {escolha_usuario}")
print(f"O Computador escolheu: {escolha_computador}")
print("-" * 50)

# --- 4. LÓGICA DO JOGO ---

# Caso de Empate
if escolha_usuario == escolha_computador:
    print("🟰 EMPATE!")

# Casos de Vitória do Usuário
# Usando 'or' para simplificar as três condições de vitória
elif (escolha_usuario == "PEDRA" and escolha_computador == "TESOURA") or \
        (escolha_usuario == "TESOURA" and escolha_computador == "PAPEL") or \
        (escolha_usuario == "PAPEL" and escolha_computador == "PEDRA"):

    print("🎉 VOCÊ VENCEU!")

# Casos de Vitória do Computador (tudo o que não for empate ou vitória do usuário)
else:
    print("🤖 O COMPUTADOR VENCEU!")

print("-" * 50)