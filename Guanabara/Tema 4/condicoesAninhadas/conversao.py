# 1. ENTRADA DO NÚMERO
try:
    numero_decimal = int(input("Digite um número inteiro positivo para conversão: "))

    if numero_decimal < 0:
        print("\nErro: Por favor, digite apenas números inteiros positivos.")
        exit()

except ValueError:
    print("\nErro: Entrada inválida. Digite um número inteiro.")
    exit()

# Variável para ser manipulada nos cálculos
numero_a_converter = numero_decimal
resultado = ""
base_destino = ""

# 2. ENTRADA DA OPÇÃO DE CONVERSÃO
print("\nEscolha a base para a qual deseja converter:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = input("Digite o número da sua escolha (1, 2 ou 3): ")

# --- 3. ESTRUTURA SE ANINHADA COM CÁLCULOS MANUAIS ---

if opcao == '1':
    # --- CONVERSÃO PARA BINÁRIO (Base 2) ---
    base = 2
    base_destino = "Binário"

    if numero_a_converter == 0:
        resultado = "0"
    else:
        while numero_a_converter > 0:
            # Pega o resto da divisão por 2 (0 ou 1)
            resto = numero_a_converter % base
            # Adiciona o resto ao início do resultado
            resultado = str(resto) + resultado
            # Atualiza o número para o quociente da divisão inteira
            numero_a_converter //= base

else:
    if opcao == '2':
        # --- CONVERSÃO PARA OCTAL (Base 8) ---
        base = 8
        base_destino = "Octal"

        if numero_a_converter == 0:
            resultado = "0"
        else:
            while numero_a_converter > 0:
                # Pega o resto da divisão por 8
                resto = numero_a_converter % base
                # Adiciona o resto ao início do resultado
                resultado = str(resto) + resultado
                # Atualiza o número para o quociente da divisão inteira
                numero_a_converter //= base

    else:
        if opcao == '3':
            # --- CONVERSÃO PARA HEXADECIMAL (Base 16) ---
            base = 16
            base_destino = "Hexadecimal"

            # Mapeamento para os dígitos de 10 a 15
            digitos_hexa = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

            if numero_a_converter == 0:
                resultado = "0"
            else:
                while numero_a_converter > 0:
                    # Pega o resto da divisão por 16
                    resto = numero_a_converter % base

                    if resto < 10:
                        # Se o resto for 0-9, usa o próprio número
                        caractere = str(resto)
                    else:
                        # Se o resto for 10-15, usa a letra correspondente
                        caractere = digitos_hexa[resto]

                    # Adiciona o caractere ao início do resultado
                    resultado = caractere + resultado
                    # Atualiza o número
                    numero_a_converter //= base

        else:
            # Opção Inválida
            resultado = "Opção de conversão inválida."
            base_destino = "Nenhuma"

# 4. SAÍDA DO RESULTADO

print("\n--- Resultado ---")
if base_destino == "Nenhuma":
    print(resultado)
else:
    print(f"Número Decimal: {numero_decimal}")
    print(f"Base de Destino: {base_destino}")
    print(f"Resultado da Conversão: {resultado}")
print("-----------------")