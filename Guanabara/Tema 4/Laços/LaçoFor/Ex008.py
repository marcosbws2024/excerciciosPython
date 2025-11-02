print("=== Verificador de Palíndromo ===")
# 1. Entrada de dados
texto = input("Digite uma palavra ou número para verificar: ")

# 2. Pré-processamento (Opcional, mas melhora a precisão para frases)
# Remove espaços, pontuação e converte para minúsculas
texto_limpo = "".join(filter(str.isalnum, texto)).lower()

# 3. Verificação
# O 'slice' [::-1] inverte a string
texto_invertido = texto_limpo[::-1]

print("-" * 30)

if texto_limpo == texto_invertido:
    print(f"'{texto}' é um PALÍNDROMO! 🥳")
else:
    print(f"'{texto}' NÃO é um palíndromo.")
    print(f"Lido ao contrário: {texto_invertido.upper()}")

print("-" * 30)