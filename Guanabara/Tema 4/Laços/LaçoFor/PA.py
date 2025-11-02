# 1. Entrada de Dados
primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
num_termos = 10  # Definimos 10 como padrão simples

# 2. Cálculo do Limite
# O limite é o primeiro termo mais (Número de termos * Razão)
# Isso garante que a sequência terá o número exato de termos desejados.
limite_de_parada = primeiro_termo + (num_termos * razao)

# 3. Geração e Exibição
print("\nSequência PA:")
# Usamos o 'primeiro_termo' como início e a 'razao' como passo (step)
for termo in range(primeiro_termo, limite_de_parada, razao):
    print(termo, end=' -> ')

print("FIM")