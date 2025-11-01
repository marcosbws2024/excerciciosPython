# Coleta dos dados
a = int(input("Digite o comprimento do lado A: "))
b = int(input("Digite o comprimento do lado B: "))
c = int(input("Digite o comprimento do lado C: "))

# Variável de controle, inicializada como False
pode_formar = False

# A condição de existência do triângulo exige que
# CADA lado seja menor que a soma dos outros dois.

# 1. VERIFICAÇÃO DE EXISTÊNCIA (Manteve sua lógica aninhada)
if a + b > c:
    if a + c > b:
        if b + c > a:
            pode_formar = True

# --- Estrutura de Saída e CLASSIFICAÇÃO ---

print("-" * 30)

if pode_formar:
    # SE o triângulo PODE ser formado, entramos no bloco de CLASSIFICAÇÃO

    print("Os comprimentos informados PODEM formar um triângulo.")

    # 2. CLASSIFICAÇÃO (Usando if/elif/else)

    if a == b and b == c:
        # A. EQUILÁTERO (Todos os lados iguais)
        print("Classificação: TRIÂNGULO EQUILÁTERO.")

    elif a == b or a == c or b == c:
        # B. ISÓSCELES (Pelo menos dois lados iguais)
        # Note: Se fosse equilátero, ele já teria parado no 'if' acima.
        print("Classificação: TRIÂNGULO ISÓSCELES.")

    else:
        # C. ESCALENO (Nenhum lado igual)
        # Se não é equilátero nem isósceles, só pode ser escaleno.
        print("Classificação: TRIÂNGULO ESCALENO.")

else:
    # Se o triângulo NÃO pode ser formado
    print("Os comprimentos informados NÃO podem formar um triângulo.")

print("-" * 30)