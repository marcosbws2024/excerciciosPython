# ====================================================================
# OBJETIVO: Encontrar números que satisfazem a propriedade de Kaprekar
# na base 100 (onde a raiz é igual à soma das duas metades do quadrado).
# ====================================================================

print("--- BUSCANDO NÚMEROS DE RAIZ 1 ATÉ 1000 ---")
print("------------------------------------------")

# Itera sobre o intervalo de possíveis raízes.
# (Raiz começa em 1 e vai até 1000. O 'stop' do range é exclusivo, por isso 1001)
for raiz in range(1, 1001):

    # 1. CALCULA O QUADRADO (O NÚMERO A SER AVALIADO)
    num = raiz * raiz

    # 2. SEPARA EM DUAS PARTES (Base 100)

    # O operador % (módulo) obtém o resto da divisão por 100,
    # que são os dois dígitos menos significativos (a 'metade direita').
    menor = num % 100

    # O operador // (divisão inteira) obtém o quociente da divisão por 100,
    # que são os dígitos mais significativos (a 'metade esquerda').
    maior = num // 100

    # 3. VERIFICA A PROPRIEDADE

    # Verifica se a soma das duas partes é igual à raiz original.
    if (menor + maior) == raiz:
        # Se a condição for satisfeita, imprime detalhadamente o resultado.
        print("\n=== NÚMERO ENCONTRADO ===")
        print("Quadrado (num): ", num)
        print("Parte Menor (menor): ", menor)
        print("Parte Maior (maior): ", maior)
        print("Raiz Original (raiz): ", raiz)
        print("Verificação: {} + {} = {} (igual à raiz)".format(maior, menor, raiz))
        print("=========================")

# Após o loop terminar, esta parte é executada apenas uma vez.
print("\nProcesso de busca finalizado.")

# A variável 'raiz' manterá o último valor testado no loop.
# Neste caso, o último valor é 1000 (o último número antes do 1001 exclusivo).
print("Última raiz testada (ao sair do loop): ", raiz)