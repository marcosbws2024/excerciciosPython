velocidade = float(input("Digite um valor: "))
limite = 80
if velocidade > 80:
    print("Voce será multado")
    velocidadeUltrapassada = velocidade - 80
    valor = velocidadeUltrapassada * 7.00
    print(f"O limite é {limite}\nFoi ultrapassado {velocidadeUltrapassada}km do limite\nO valor da multa é R$7,00 por km\nValor da Multa R${valor}")

print("Não ultrapassou a velocidade")