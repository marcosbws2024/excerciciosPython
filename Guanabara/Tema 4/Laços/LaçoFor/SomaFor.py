valor=[]
soma =0
for i in range(0,4):
    entrada = int(input(f"Digite o valor {i+1}: "))
    valor.append(entrada)
    soma =soma + entrada
print(f"O resultado da Soma:{soma}")