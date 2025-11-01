num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um número inteiro: "))
num3 = int(input("Informe um número inteiro: "))

# --- Descobrir o maior ---
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# --- Descobrir o menor ---
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("Maior número entre {}, {} e {} é {}".format(num1, num2, num3, maior))
print("Menor número entre {}, {} e {} é {}".format(num1, num2, num3, menor))

