while True:
    try:
        num = eval(input("Entre com um número inteiro: "))
        print(num)
        break
    except (ValueError, NameError, SyntaxError):
        print("Valor Inválido!!!")
