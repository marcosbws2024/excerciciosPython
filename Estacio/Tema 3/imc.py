nome = "Alice"
idade = 30
peso = 0.0  # Inicializando com float para consistência
altura = 0.0
imc = 0.0

try:
    # 1. TENTA obter as entradas do usuário
    altura = float(input("Digite a altura em metros: "))
    peso = float(input("Digite o seu peso: "))

    # 2. Verifica a validade dos dados APÓS a entrada
    if peso > 0 and altura > 0:
        # 3. Cálculo do IMC só ocorre se os valores forem válidos
        imc = peso / (altura ** 2)

        # --- Saída de Sucesso ---
        print("\n--- Resultado do IMC ---")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Altura: {altura:.2f}m")
        print(f"Peso: {peso:.1f}kg")
        print(f"IMC: {imc:.2f}")

    else:
        # 4. Trata valores não-positivos (ex: 0, -1)
        print("\nERRO: Valores de Altura e Peso devem ser maiores que zero.")
        imc = 0.0  # Define imc para evitar erro se for referenciado depois

# 5. Captura erro se a entrada NÃO PUDER ser convertida para float (ex: digitar 'a')
except ValueError:
    print("\nERRO DE ENTRADA: Por favor, digite números válidos para peso e altura.")
    imc = 0.0

except Exception as e:
    print(f"\nERRO INESPERADO: {e}")
    imc = 0.0

""" teste de comentario de multiplas linhas
 assim podemos escrever comentarios a vontade"""