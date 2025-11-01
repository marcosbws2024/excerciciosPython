# Coleta dos dados
a = int(input("Digite o comprimento do lado A: "))
b = int(input("Digite o comprimento do lado B: "))
c = int(input("Digite o comprimento do lado C: "))

# Variável de controle, inicializada como False
pode_formar = False

# A condição de existência do triângulo exige que
# CADA lado seja menor que a soma dos outros dois.

# 1. Primeira Condição
if a + b > c:

    # 2. Segunda Condição (testada somente se a primeira for True)
    if a + c > b:

        # 3. Terceira Condição (testada somente se as duas anteriores forem True)
        if b + c > a:
            # Se chegamos aqui, todas as 3 condições são VERDADEIRAS
            pode_formar = True

# --- Saída do Resultado ---

if pode_formar:
    print("Os comprimentos informados PODEM formar um triângulo.")
else:
    print("Os comprimentos informados NÃO podem formar um triângulo.")