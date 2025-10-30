salario = float(input("Digite o valor do Salário: "))

abono = (salario * 15) / 100
novosalario = salario + abono
print("Salario com Aumento: R${:.2f}".format(novosalario))
print("Valor do Aumento: R${:.2f}".format(abono))
