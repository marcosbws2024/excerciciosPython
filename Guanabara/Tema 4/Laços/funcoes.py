CONSTANTE = 8

def somar(a,b):
     soma = a + b
     return soma

def subtracao(a,b):
     subtracao = a - b
     return subtracao

def  multiplicacao(a,b):
     multiplicacao = a * b
     return multiplicacao
  
def divisao(a,b):
    try:
        divisao = a/b
        return divisao
    except ValueError:
        print("Valor Invalido!!!")
    except ZeroDivisionError:
        print("Não Existe de divisao por Zero!!!")
    except TypeError:
        print("Esse valor não é valido!!!")
    
print("=*="*CONSTANTE)   
print("Soma:",somar(5,3))
print("Multiplicação:",multiplicacao(8,5))
print("Subtração:",subtracao(20,15))
print("Divisão:", divisao(15,3))
print("=*="*CONSTANTE)   
        