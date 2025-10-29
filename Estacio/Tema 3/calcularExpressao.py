def calcular_expressao():
    expressao = input("Digite uma expressão matemática: ")

    try:

        resultado = eval(expressao)

        print(f"O resultado da expressão: {resultado}")
    except Exception as e:
        print(f"Erro ao avaliar a expressão matemática: {e}")


calcular_expressao()