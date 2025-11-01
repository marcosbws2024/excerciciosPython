nota1 = float(input("Valor 1: "))
nota2 = float(input("Valor 2: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado")
elif media >= 5 and media < 6.9:
    print("Recuperacao")
else:
    print("Aprovado")