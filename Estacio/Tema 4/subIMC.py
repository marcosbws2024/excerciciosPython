def calculaIMC(peso,altura):
    return peso*100 / (altura *2)

peso = eval(input("Digite o peso: "))
altura = eval(input("Digite o Altura: "))
imc = calculaIMC(peso,altura)
print("IMC: {:.2f}".format(imc))