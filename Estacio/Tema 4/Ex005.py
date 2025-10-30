numeros=[1, 2, 3, 4]

for n in numeros:
    quadrado = n * 2
    print(f'{n}^2 = {quadrado}')
print("*" * 30)

somanumeros=[1, 2, 3, 4]

somatorio = 0
for somanum in somanumeros:
        somatorio += somanum
print(somatorio)

print("*" * 30)
numero_tabuada = 5
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    resultado = numero_tabuada * n

    # Imprime no formato: 5 x 1 = 5
    print(f'{numero_tabuada} x {n} = {resultado}')
print("*" * 30)

texto = 'programacao'
letraparacontar='r'
contador = 0
for letra in texto:
    if letraparacontar == letra:
        contador += 1

print(f'A quantidade de letra {letraparacontar} é {contador}')

print("*" * 30)
for numero in range(11):
    print(numero)

    print("*" * 30)
numero = 5
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')