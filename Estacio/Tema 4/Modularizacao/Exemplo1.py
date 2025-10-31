# Exemplo de uso de modulos
# Calcular as Raizes de uma equação do segundo grau

import math # Módulo correto!

# funcao para calcular as raizes de uma equacao de segundo grau
def calcularRaizes(a,b,c):
# calcula o discriminante
   delta = b**2 -4 * a * c

# verifica-se o discriminante é positivo,negativo ou zero
   if delta > 0:
       # Duas raizes reais e distintas
       # CORRIGIDO: math.sqrt
       raiz1 = (-b + math.sqrt(delta))/(2*a)
       # CORRIGIDO: math.sqrt e o sinal de -
       raiz2 = (-b - math.sqrt(delta))/(2*a) 
       return (raiz1,raiz2)
       
   elif delta==0:
        # Uma raiz real (duas raizes reais e iguais)
        raiz = -b / (2*a)
        return (raiz,)
        
   else:
       # Raizes complexas (discriminante negativo)
       parteReal = -b /(2*a)
       # CORRIGIDO: math.sqrt
       parteImaginaria = math.sqrt(-delta)/(2*a)
       raiz1 = complex(parteReal,parteImaginaria)
       # Raiz complexa conjugada
       raiz2 = complex(parteReal, -parteImaginaria) 
       # CORRIGIDO: Adicionado o 'return'
       return (raiz1, raiz2) 
       
# solicitando os coeficientes ao usuario.
a = float(input("Digite o coeficiente de a: "))
b = float(input("Digite o coeficiente de b: "))
c = float(input("Digite o coeficiente de c: "))

# calculando raizes
raizes = calcularRaizes(a,b,c)

# imprimindo resultados.
if len(raizes) == 2:
  print(f"As raizes da equação são: {raizes[0]:.2f} e {raizes[1]:.2f}") 
else:
    # Esta parte é usada apenas se delta é zero (raiz única)
 print(f"A raiz da equação é: {raizes[0]:.2f}")