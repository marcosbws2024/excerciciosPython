# 1. Entrada de Dados
try:
    valor = int(input("Digite um número inteiro para verificar se é primo: "))
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
    exit()

# 2. Casos Especiais e Números Inválidos
if valor <= 1:
    print(f"{valor} NÃO É PRIMO, pois números primos são maiores que 1.")
    
# 3. Lógica Principal: Verificação de Divisores
# Supomos inicialmente que o número é primo
elif valor > 1:
    e_primo = True
    
    # Testamos a divisibilidade por todos os números entre 2 e (valor - 1)
    # Se for divisível por QUALQUER um, ele NÃO é primo.
    for divisor in range(2, valor):
        if valor % divisor == 0:
            e_primo = False  # Encontramos um divisor! Não é primo.
            break            # Paramos o loop imediatamente (otimização)

    # 4. Saída
    if e_primo:
        print(f"O número {valor} É PRIMO!")
    else:
        print(f"O número {valor} NÃO É PRIMO.")
        print(f"Ele é divisível por {divisor} (além de 1 e ele mesmo).")