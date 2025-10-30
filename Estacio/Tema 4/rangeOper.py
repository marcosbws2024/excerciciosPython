# --- Demonstração do Range() ---
print("### 1. Exemplos da função range() ###")

# 1. Range com 1 argumento (stop): range(N) -> de 0 até N-1
# Sequência: 0, 1, 2
print("\nRange(3):")
for i in range(3):
    print(i, end=" ")
print("\n")

# 2. Range com 2 argumentos (start, stop): range(A, B) -> de A até B-1
# Sequência: 2, 3, 4, 5, 6
print("Range(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print("\n")

# 3. Range com 3 argumentos (start, stop, step): range(A, B, C) -> de A, pulando de C em C, até B-1
# Sequência: 2, 5, 8
print("Range(2, 9, 3):")
for i in range(2, 9, 3):
    print(i, end=" ")
print("\n" + "="*40)


# --- Demonstração de Operadores Sequenciais ---

# Strings são sequências de caracteres, então podemos usar esses operadores
s = "Python"
t = " rocks"
n = 3

print("### 2. Exemplos de Operadores Sequenciais ###")

# 1. x in s (Verifica a presença)
caractere = 'y'
existe = caractere in s
print(f"'{caractere}' in '{s}'? -> {existe}") # Saída: True

sub_string = "tho"
existe = sub_string in s
print(f"'{sub_string}' in '{s}'? -> {existe}") # Saída: True

# 2. s + t (Concatenação)
concatenacao = s + t
print(f"'{s}' + '{t}' = '{concatenacao}'")
# Saída: 'Python' + ' rocks' = 'Python rocks'

# 3. n * s (Repetição)
repeticao = n * s
print(f"{n} * '{s}' = '{repeticao}'")
# Saída: 3 * 'Python' = 'PythonPythonPython'

# 4. len(s) (Comprimento)
comprimento = len(s)
print(f"Comprimento de '{s}': {comprimento}") # Saída: 6

# 5. s[i] (Acesso por índice)
primeira_letra = s[0]
ultima_letra = s[-1]
print(f"Primeira letra (índice 0): {primeira_letra}") # Saída: P
print(f"Última letra (índice -1): {ultima_letra}")   # Saída: n

# 6. min(s) e max(s) (Ordem do dicionário/alfabética)
menor = min(s) # O caractere com o menor valor ASCII/alfabético
maior = max(s) # O caractere com o maior valor ASCII/alfabético
print(f"Menor caractere (alfabético) em '{s}': {menor}") # Saída: P (ou H, dependendo da ordem)
print(f"Maior caractere (alfabético) em '{s}': {maior}") # Saída: y