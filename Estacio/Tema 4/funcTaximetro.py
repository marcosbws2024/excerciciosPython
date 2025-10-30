def taximetro (distancia):
    def calcularMult():
        if distancia <5:
            return 1.2
        else:
            return 1

    multiplicador = calcularMult()
    largada = 3
    kmRodado = 2
    valor = (largada + distancia * kmRodado) * multiplicador
    return valor

distancia = eval(input('Digite a distancia em km: '))
pagamento  = taximetro(distancia)
print(pagamento)