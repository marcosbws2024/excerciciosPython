#criando uma lista com alguns elementos
lista= [10,20,30,40,50]

#acessando elementos individuais
primeiroElemento = lista[0]
segundoElemento = lista[1]

#imiprimindo os elementos acessados
print(f'primeiro elemento: {primeiroElemento}')
print(f'segundo elemento: {segundoElemento}')

#Adicionando um elemento ao final da lista
lista.append(60)
print(f'Lista apos adicionar 60: {lista}')

#inserindo um elemento em uma posicao especifica
lista.insert(2,25)#inserindo 25 na posicao 2
print(f'Lista apos adicionar 25: {lista}')

#removendo um elemento da lista
lista.remove(40) #remove o primeiro valor 40 encotrado
print(f'Lista apos remover 40: {lista}')

#removendo o ultimo elemento da lista
ultimoElemento = lista.pop()
print(f'ultimo elemento removido que é 60: {lista}')

#Acessando um subgrupo da lista (fatiamento)
sublista = lista[1:4]
print(f'Lista apos remover 4: {sublista}')

#ordenando a lista
lista.sort()
print(f'Lista Ordenada: {lista}')

#iterando sobre os elementos da lista
for elemento in lista:
    print(elemento)



