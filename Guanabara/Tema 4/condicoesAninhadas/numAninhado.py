a = int(input("Valor 1: "))
b = int(input("Valor 2: "))

if a > b:
    print("O valor {} é maior que o valor {}".format(a,b))
elif a == b:
    print("Os valores são iguais")
elif b > a:
    print("O valor {} é maior que o valor {}".format(b,a))
else:
    print("Não foi digitado um numero valido!!!")
