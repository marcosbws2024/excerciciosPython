salario = float(input("Digite seu Salario: R$"))

if(salario > 1250):
    abono = (salario *10) /100
    salario = salario +abono
else:
    abono = (salario * 15) /100
    salario = salario + abono
print("*" * 30)
print(f"O seu Salario teve um aumento de:{abono} ")
print(f"O seu novo salário é:{salario} ")