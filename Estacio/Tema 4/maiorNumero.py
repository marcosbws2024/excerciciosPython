"""
listaNumero = [45,456,489,12,48,34,36]
maiorElemento = listaNumero[0]
for n in listaNumero:
    if n > maiorElemento:
      maiorElemento = n

print(f'Maior numero: {maiorElemento}')
"""


def maiorNumero(lista):
    if not lista:
        return None

    maiorElemento = lista[0]

    for n in lista:
        if n > maiorElemento:
            maiorElemento = n

    return maiorElemento

listaNumero = [45, 456, 489, 12, 48, 34, 36]
resultado = maiorNumero(listaNumero)
print(f'Lista utilizada: {listaNumero}')
print(f'Maior numero encontrado: {resultado}')