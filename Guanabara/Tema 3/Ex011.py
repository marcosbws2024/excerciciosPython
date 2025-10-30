valor = float(input("Digite um valor em Reais R$:"))
cotacaodolar= float(input("Digite a cotacao do Dolar: "))

convertido = valor/cotacaodolar
print("Você pode obter US${:.2f} dolares".format(convertido))