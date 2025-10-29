def calcular_compra():
    """
    Solicita a quantidade de produtos ao usuário, calcula o total da compra
    e trata erros de entrada.
    """

    # === 1. Atribuição: Definição dos Preços Unitários (Constantes) ===
    PRECOS = {
        "Arroz (5kg)": 25.99,
        "Feijão (1kg)": 8.50,
        "Leite (L)": 4.25,
        "Pão Francês (un)": 0.75
    }

    print("=" * 40)
    print("      CAIXA SIMULADO DO SUPERMERCADO")
    print("=" * 40)

    # Inicializa o total da compra
    preco_total = 0.0

    try:
        # === 2. Entrada de Dados: Solicitação das Quantidades ===

        print("\n--- Digite a quantidade desejada de cada item (apenas números inteiros) ---")

        # O loop percorre cada item e seu preço no dicionário PRECOS
        for item, preco_unitario in PRECOS.items():

            # Formata o preço unitário para exibição no prompt
            preco_formatado = f"R$ {preco_unitario:.2f}"

            # Pede a entrada, garantindo que seja um número inteiro
            quantidade_str = input(f"Quantidade de {item} ({preco_formatado}): ")

            # Converte a entrada para inteiro. Se falhar, o bloco 'except ValueError' será ativado
            quantidade = int(quantidade_str)

            # Garante que a quantidade não seja negativa
            if quantidade < 0:
                print("Aviso: Quantidade não pode ser negativa. Usando 0.")
                quantidade = 0

            # === 3. Cálculo do Total ===
            subtotal = preco_unitario * quantidade
            preco_total += subtotal

        # === 4. Saída de Dados: Exibição do Resultado ===
        print("-" * 40)
        print("CÁLCULO FINALIZADO")

        # Formata o preço final para duas casas decimais (moeda)
        print(f"O preço total da sua compra é: R$ {preco_total:.2f}")
        print("=" * 40)

    # Tratamento de Erro para entradas não numéricas nas quantidades
    except ValueError:
        print("\nERRO DE ENTRADA: Por favor, digite apenas números inteiros para as quantidades.")
        print("O cálculo foi interrompido.")

    except Exception as e:
        print(f"\nERRO INESPERADO: Ocorreu um erro: {e}")


# Executa o programa
calcular_compra()
