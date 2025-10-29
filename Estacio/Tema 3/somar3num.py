print("Por favor, digite as três notas em formato numérico.")
print("-------------------------------------------------------")

try:
    # Tenta obter as três notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Se todas as entradas forem válidas, calcula a média
    media = (nota1 + nota2 + nota3) / 3

    # Mostra o resultado
    print(f"\nA media das notas é: {media:.2f}")

# Captura o erro se qualquer uma das entradas não puder ser convertida para float
except ValueError:
    print("\nERRO DE ENTRADA: Uma das notas digitadas nao e um numero valido.")
    print("O programa foi encerrado.")

except Exception as erro:
    print(f"Erro inesperado: {erro}")
