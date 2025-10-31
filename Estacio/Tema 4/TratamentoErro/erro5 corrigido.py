# Correção do erro de tipo: conversão da letra para número antes da soma
numero = 10
letra = 'a'

# Convertendo a letra para um número inteiro usando a função ord()
numero_letra = ord(letra) - ord('a') + 1

# Realizando a soma corretamente
resultado = numero + numero_letra
print(resultado)