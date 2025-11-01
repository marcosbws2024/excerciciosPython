import random
from time import sleep

while True:
    num = random.randint(0, 5)

    print("Adivinha o valor entre 0 e 5 ")
    valor = int(input("Digite um valor: "))
    print("Pensando...")
    sleep(3)
    if valor == num:
         print("Voce Acertou")
         break
    else:
        print("Voce errou")
