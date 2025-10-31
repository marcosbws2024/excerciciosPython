import numpy as np 
#bibloioteca externa

def calcularRaizes(a,b,c):
    coeficientes = [a,b,c]
    
    raizes  = np.roots(coeficientes)
    return raizes

a = float(input("Valor a: "))
b = float(input("Valor b: "))
c = float(input("Valor c: "))

raizes = calcularRaizes(a,b,c)
print(f"As raizes da Equação são: {raizes[0]} e {raizes[1]}")