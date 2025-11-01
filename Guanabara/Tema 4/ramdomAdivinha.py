import random

while True:
    num = random.randint(0, 5)  # Gera um número entre 1 e 10 (inclusive)

    print("Adivinha o valor entre 0 e 5 ")
    valor = int(input("Digite um valor: "))
    if valor == num:
         print("Voce Acertou")
         break
    else:
        print("Voce errou")
