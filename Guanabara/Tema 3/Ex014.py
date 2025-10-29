valorcompra = float(input("Digite o valor da Compra: "))

desconto = (valorcompra * 5) / 100
novopreco = valorcompra - desconto
print("Valor com desconto: {}".format(novopreco))
