def divide(a, b):
    return a / b

try:
    resultado = divide(10, 0)
except ZeroDivisionError as ex:
    print(f"Erro: {ex}") 