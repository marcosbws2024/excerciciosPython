# 1. ENTRADA DO NÚMERO
try:
    numero_decimal = int(input("Digite um número inteiro positivo para conversão: "))

    if numero_decimal < 0:
        print("\nErro: Por favor, digite apenas números inteiros positivos.")
        exit()

except ValueError:
    print("\nErro: Entrada inválida. Digite um número inteiro.")
    exit()

# 2. ENTRADA DA OPÇÃO DE CONVERSÃO
print("\nEscolha a base para a qual deseja converter:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opcao = input("Digite o número da sua escolha (1, 2 ou 3): ")

# --- 3. ESTRUTURA CONDICIONAL SIMPLIFICADA (USANDO ELIF) ---

resultado = ""
base_destino = ""

if opcao == '1':
    # Binário: bin() + [2:] remove o prefixo '0b'
    resultado = bin(numero_decimal)[2:]
    base_destino = "Binário"

elif opcao == '2':
    # Octal: oct() + [2:] remove o prefixo '0o'
    resultado = oct(numero_decimal)[2:]
    base_destino = "Octal"

elif opcao == '3':
    # Hexadecimal: hex() + [2:] remove '0x' e .upper() coloca as letras em maiúsculo
    resultado = hex(numero_decimal)[2:].upper()
    base_destino = "Hexadecimal"

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