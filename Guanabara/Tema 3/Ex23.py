diasAlugados = int(input("Quantidade dias Alugados: "))
kmrodados = float(input("Quantidade Km rodados: "))

diaria = 60
dia = 0.15

valorCobrado = (diasAlugados * diaria) + (kmrodados * dia)
print("Valor da Cobrado: R${:.2f}" .format(valorCobrado))

