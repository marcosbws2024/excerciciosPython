distanciaemkm  = int(input("Informa a distancia da viagem em km: "))
viagemate200 = 0.50
viagemAcimade200 = 0.45

if distanciaemkm <= 200:
    valor = distanciaemkm * viagemate200
else:
    valor = distanciaemkm * viagemAcimade200

print(valor)