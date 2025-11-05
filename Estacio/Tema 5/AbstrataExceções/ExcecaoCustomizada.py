class ExcecaoCustomizada(Exception):
    pass

def checa_valor(valor):
    if valor < 0:
        raise ExcecaoCustomizada("Valor não pode ser negativo!")

def divide(a, b):
    return a / b


try:
    resultado = divide(10, 0)
except ZeroDivisionError as ex:
    print(f"Erro de divisão por zero: {ex}")

try:
    checa_valor(-10)
except ExcecaoCustomizada as ex:
    print(f"Exceção personalizada lançada: {ex}")