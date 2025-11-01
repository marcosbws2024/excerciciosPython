import time

menor = 0
idadePassou = 0
anoAtual = int(time.strftime("%Y"))

# --- Entrada e Cálculo ---
try:
    anoNasc = int(input("Digite o ano de nascimento: "))
    idade = anoAtual - anoNasc

    # --- Estrutura Condicional Corrigida ---

    if idade < 17:
        menor = 17 - idade
        print("Faltam {} anos para poder se alistar".format(menor))

    elif idade >= 17 and idade < 46:
        print("Pode se Alistar")

    elif idade > 45:
        # CORREÇÃO DA INDENTAÇÃO APLICADA AQUI (ambas as linhas com o mesmo recuo)
        idadePassou = idade - 45
        print(f"Não pode se Alistar, voce passou {idadePassou} anos da idade de se alistar")

    else:
        print("Inválido")

except ValueError:
    print("ERRO: Por favor, digite um ano de nascimento válido (apenas números).")
