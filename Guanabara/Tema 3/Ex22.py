# 1. Solicita a temperatura em Celsius
celsius = input("Digite a temperatura em graus Celsius (°C): ")

try:
    # Converte a entrada para um número decimal (float)
    celsius = float(celsius)

    # 2. Aplica a fórmula de conversão
    #fahrenheit = (celsius * 1.8) + 32
    fahrenheit = (9*celsius /5) + 32

    # 3. Imprime o resultado formatado
    print("-" * 60)
    print(f"A temperatura de {celsius:.2f}°C equivale a {fahrenheit:.2f}°F.")
    print("-" * 60)

except ValueError:
    # Captura erro se o usuário digitar algo que não é um número
    print("Erro: Por favor, digite um valor numérico válido.")