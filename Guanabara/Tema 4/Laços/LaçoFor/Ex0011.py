# Inicialização das variáveis para os cálculos
soma_idades = 0          # Para calcular a média
homem_mais_velho = ""    # Nome do homem mais velho
idade_homem_mais_velho = -1 # Idade do homem mais velho (começa com -1 para garantir a primeira comparação)
total_mulheres_jovens = 0 # Contador de mulheres com menos de 20 anos
NUMERO_DE_PESSOAS = 5

print("--- Análise de Dados de 5 Pessoas ---")

# Loop para ler e processar os dados de 5 pessoas
for i in range(1, NUMERO_DE_PESSOAS + 1):
    print(f"\n--- Dados da Pessoa {i} ---")
    
    # 1. Leitura do Nome (String)
    nome = input("Nome: ").strip()

    # 2. Leitura da Idade (Garantindo que seja um número inteiro positivo)
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            else:
                print("Idade deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Digite a idade em número inteiro.")

    # 3. Leitura do Sexo (Garantindo que seja M ou F)
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'M' para Masculino ou 'F' para Feminino.")

    # A. CÁLCULO DA MÉDIA
    soma_idades += idade

    # B. HOMEM MAIS VELHO
    if sexo == 'M':
        # Compara a idade lida com a idade do homem mais velho registrada até agora
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome

    # C. MULHERES JOVENS
    if sexo == 'F':
        # Verifica se a idade é menor que 20
        if idade < 20:
            total_mulheres_jovens += 1

# --- RESULTADOS FINAIS ---

# Calcula a média da idade
media_idade = soma_idades / NUMERO_DE_PESSOAS

print("\n" + "=" * 40)
print("              RELATÓRIO DE ANÁLISE")
print("=" * 40)

# Requisito 1: Média de Idade
print(f"1. A Média de Idade do grupo é: {media_idade:.1f} anos")

# Requisito 2: Homem Mais Velho
if homem_mais_velho:
    print(f"2. O Homem mais velho é: {homem_mais_velho} com {idade_homem_mais_velho} anos")
else:
    print("2. Nenhum homem foi registrado.")

# Requisito 3: Mulheres Jovens
print(f"3. Total de Mulheres com menos de 20 anos: {total_mulheres_jovens}")
print("=" * 40)