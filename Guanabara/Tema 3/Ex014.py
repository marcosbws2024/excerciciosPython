valorcompra = float(input("Digite o valor da Compra R$: "))

desconto = (valorcompra * 5) / 100
novopreco = valorcompra - desconto
print("Valor com desconto: R${:.2f}".format(novopreco))
print("Valor do desconto: R${:.2f}".format(desconto))
