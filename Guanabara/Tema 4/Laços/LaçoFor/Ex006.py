# --- 1. Entrada de Dados ---

print("=== Calculadora de Progressão Aritmética (PA) ===")

# Leitura do primeiro termo (a1)
# Usamos int() para garantir que a entrada seja um número inteiro
try:
    primeiro_termo = int(input("Digite o PRIMEIRO TERMO da PA: "))
except ValueError:
    print("Entrada inválida. O primeiro termo deve ser um número inteiro.")
    exit()

# Leitura da razão (r)
try:
    razao = int(input("Digite a RAZÃO da PA: "))
except ValueError:
    print("Entrada inválida. A razão deve ser um número inteiro.")
    exit()

# Definimos quantos termos queremos exibir
quantidade_termos = 10 

# --- 2. Geração e Exibição da PA ---

print("-" * 40)
print(f"Os {quantidade_termos} primeiros termos da PA são:")

# O último termo que queremos alcançar é calculado pela fórmula do termo geral:
# an = a1 + (n - 1) * r
ultimo_termo = primeiro_termo + (quantidade_termos - 1) * razao

# No Python, range(start, stop, step) o 'stop' é EXCLUSIVO, 
# então adicionamos a razão ao 'ultimo_termo' para garantir que ele seja incluído.
# O 'step' (passo) é exatamente a razão.
for termo in range(primeiro_termo, ultimo_termo + razao, razao):
    # Imprime cada termo seguido por uma seta, sem quebrar a linha (end=' -> ')
    print(f'{termo}', end=' -> ')

print("FIM") 
print("-" * 40)