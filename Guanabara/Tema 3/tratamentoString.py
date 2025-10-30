frase = "Curso em Video Python"
#fatiamento de String
print(frase[0:6])#sem um a menos no final
print(frase[9:14])#sem um a menos no final
print(frase[9:21])#sem um a menos no final
print(frase[9:21:2])#Saltando de dois em dois
print(frase[:5])#inicia do 0 ocultando
print(frase[15:])#sem saber o final vai até o final
print(frase[9::3])#comeca do nove ate o final pulando de 3 em 3
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,14))
print(frase.find('deo'))#mostra a posicao que comeca o deo começando em d
print(frase.find('Android')) #Valor -1 (Não existe a String)
print('Curso' in frase)
print(frase.replace('Python','iOS'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #somente a primeira letra fica maiuscula
print(frase.title()) #analisa todas as palavras e deixa a primeira letra de cada palavra
print(frase.strip()) #tira o valores vazios de inicio e fim da frase
print(frase.rstrip()) #remove o espaco somente no fim
print(frase.lstrip()) #remove o espaco somente da direita
print(frase.strip())
print('-'.join(frase))