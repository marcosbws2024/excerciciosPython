class ExcecaoCustomizada(Exception):
    pass

def divide(a,b):
   try:
    div = a/b
    return div
   except ZeroDivisionError as ex:
       print("Não Existe divisão por Zero!!!")
       print(f"Erro: {ex}")

def checaValor(valor):
    if valor<0:
        raise ExcecaoCustomizada("Valor não pode ser Negativo!")

try:
    checaValor(-10)
except ExcecaoCustomizada as ex:
    print(f"Exceção Lançada: {ex}")
        
print(f"Resuldado da Divisão: {divide(4,0)}")