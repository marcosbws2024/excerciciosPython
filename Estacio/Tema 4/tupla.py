#tuplas

tuplaHeteronea = (1,"Olá",3.14,[10,20,30],{'chave':'valor'})
#imprimindo valores individuais da tupla
print(f'tuplaHeteronea: {tuplaHeteronea[0]}')
print(f'String: {tuplaHeteronea[1]}')
print(f'Float:  {tuplaHeteronea[2]}')
print(f'Lista:  {tuplaHeteronea[3]}')
print(f'Dicionario:  {tuplaHeteronea[4]}')

#modificando a lista dentro da tupla
tuplaHeteronea[3].append(40)
print(f'tuplaHeteronea Modificada: {tuplaHeteronea[3]}')

#acesando o dicionario dentro da tupla
valorDicionario = tuplaHeteronea[4]['chave']
print(f'valor dentro do Dicionario: {valorDicionario}')

#iterando sobre a tupla e imprimindo cada elemento
for elemento in tuplaHeteronea:
    print(f'{elemento} Tipo: {type(elemento)}')