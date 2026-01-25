from datetime import datetime

frutas = ['maçã', 'banana', 'cereja', 'damasco']

for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de Letras: {len(fruta):3}"
    print(minha_fruta)

print()

p1 = 3.1415
meu_numero = f"O valor de PI é : {p1:.1f}"
meu_numero_deslocado = f"O numero PI deslocado é: {p1:6.1f}"
meu_numero_preciso = f"O numero PI mais preciso é: {p1:.4f}"
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data  = datetime.now()
minha_data = f"A data de hoje é {data}"
minha_data_formatada = f"Data formatada: {data:%d/%m/%Y}"

print(minha_data)
print(minha_data_formatada)