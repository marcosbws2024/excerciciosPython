def soma_numeros(a,b):
    soma = 0

    if isinstance(a, bool) or isinstance(b, bool):
        print("Erro: Valores booleanos (True/False) não são permitidos.")
        return None

    try:
        soma = float(a) + float(b)
        return soma
    except TypeError:
        print("Erro entrada de dados")

    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    return None

print(soma_numeros(5.0,5.0))
print(soma_numeros("e",5.0))
print(soma_numeros(True,5.0))
