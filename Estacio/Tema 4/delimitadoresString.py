texto = "Olá,Mundo!"

#acessando caracteres individuais
primeirocaracter = texto[0]
ultimocaracter = texto[-1]

print(f'primeiro caractere é {primeirocaracter}')
print(f'ultimo caractere é {ultimocaracter}')

#fatiando String
subTexto = texto[5:10]
print(f'subTexto(indices de 5 a 9): {subTexto}')

#concatenanco String
saudacao = "Olá"
nome = "Alice"
frase = saudacao + ',' + nome + '!'
print(f'Frase concatenada {frase}')

#dividindo a String em uma lista
listaPalavras = texto.strip().split()
listaPalavras = listaPalavras # Esta linha não altera nada, é redundante.
print(f'Lista de palavras: {listaPalavras}')

#substituindo partes de uma String
textoModificado  = texto.replace("Mundo","Python")
print(f'Texto modificado: {textoModificado}')

#convertendo para maiusculas e minusculas
textoMaiuscula = texto.upper()
textoMinuscula = texto.lower()
print(f'Texto Maiusculo: {textoMaiuscula}')
print(f'Texto Minusculo: {textoMinuscula}')

#removendo espacos  em branco strip()
textoEspacos = " Olá,Mundo! "
textoSemEspacos = texto.strip()
print(f'Texto Espacos: {textoSemEspacos}')

#verificando a presenta de substring
if "Mundo" in texto:
    print('A palavra Mundo foi encontrada no texto')

#formatacao de Strings
idade = 30
cidade = "São Paulo"

fraseFormatada = f'Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.'
print(f'Frase formatada: \n{fraseFormatada}')