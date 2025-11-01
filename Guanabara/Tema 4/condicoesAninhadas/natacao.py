import time

# Obtém o ano atual como um inteiro
anoAtual = int(time.strftime("%Y"))

# --- Entrada e Cálculo ---
try:
    ano = int(input("Ano de nascimento: "))

    # Validação simples do ano
    if ano > anoAtual:
        print("Erro: O ano de nascimento não pode ser futuro.")
        exit()

    idade = anoAtual - ano

    print(f"\nO atleta tem {idade} anos.")
    print("-" * 30)

    # --- Estrutura de Classificação (Otimizada com elif) ---

    if idade <= 9:
        print("Categoria: MIRIM")

    elif idade <= 14:
        # Se chegou aqui, idade é > 9 e <= 14
        print("Categoria: INFANTIL")

    elif idade <= 19:
        # Se chegou aqui, idade é > 14 e <= 19
        print("Categoria: JUNIOR")

    elif idade <= 20:
        # Se chegou aqui, idade é > 19 e <= 20
        print("Categoria: SENIOR")

    else:  # idade >= 21
        # Se chegou aqui, idade é > 20 (ou seja, >= 21)
        print("Categoria: MASTER")

except ValueError:
    print("ERRO: Por favor, digite um ano de nascimento válido (apenas números inteiros).")