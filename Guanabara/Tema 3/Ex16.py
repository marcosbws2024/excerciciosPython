nome = input("Digite seu nome completo: ")
print(nome.upper())
print(nome.lower())
#nome sendo contado sem espacos
nomeSemEspaco = nome.replace(" ", "")
print(len(nomeSemEspaco.strip()))
#primeiro nome separado com a contagem.
nomeseparado = nome.split()
primeiroNome = nomeseparado[0].strip()
print(f'O primeiro nome {primeiroNome} tem { len(primeiroNome)} letras')
