
valor_casa = float(input("Qual o valor da casa (R$)? "))
valor_salario = float(input("Qual o salário bruto mensal (R$)? "))
anos_pagamento = int(input("Quantos anos de pagamento? "))

quantidade_meses = anos_pagamento * 12
parcela_minima = valor_casa / quantidade_meses
limite_compra = (valor_salario * 30) / 100

print("-" * 50)
print(f"Parcela MÍNIMA Estimada para comprar a Casa: R$ {parcela_minima:.2f}")
print(f"Seu Limite Máximo de Parcela (30% da Renda): R$ {limite_compra:.2f}")
print("-" * 50)

# Estrutura condicional para decidir se a compra é aprovada ou não
if parcela_minima > limite_compra:
    print("NÃO CONSEGUE COMPRAR.")
else:
    print("CONSEGUE COMPRAR.")