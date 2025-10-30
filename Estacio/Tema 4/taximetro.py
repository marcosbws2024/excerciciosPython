def taximetro(distancia,multiplicador=1):
    largada = 3
    kmRodado = 2
    valor= (largada + distancia *kmRodado) * multiplicador
    return valor

pagamento = taximetro(3.5,2)
print(pagamento)
