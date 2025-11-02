soma = 0
for i in range(0,5):
    valor = int(input(f"Valor {i+1}: "))
    if valor%2==0:
        soma+=valor
        
print("A soma dos pares é :{}".format(soma))
