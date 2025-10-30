altura = float(input("Digite sua altura da parede: "))
largura = float(input("Digite sua largura da parede: "))

area = altura*largura
qtdeTinta = area/2
print('Area da Parede {:.2f}m²' .format(area))
print("Serão necessarios {:.2f} litros de tinta" .format(qtdeTinta))
