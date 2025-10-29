def calcular_compra_variaveis():
    """
    Calcula o total da compra usando variáveis separadas para cada produto.
    Inclui tratamento de erros de entrada (apenas para o primeiro item, como demonstração).
    """

    # === 1. Atribuição: Definição dos Preços Unitários ===
    hamburguer_preco = 10.50
    batata_preco = 4.00
    refrigerante_preco = 3.00

    print("=" * 40)
    print("      CAIXA SIMULADO DO SUPERMERCADO")
    print("=" * 40)

    # Inicializa as variáveis de quantidade
    q_hamburguer = 0
    q_batata = 0
    q_refrigerante = 0

    try:
        # === 2. Entrada de Dados: Solicitação das Quantidades ===

        print("\n--- Digite a quantidade desejada de cada item (apenas inteiros) ---")

        # Entrada do Hambúrguer (com tratamento de erro)
        q_hamburguer_str = input(f"Quantidade de Hambúrgueres (R$ {hamburguer_preco:.2f}): ")
        q_hamburguer = int(q_hamburguer_str)

        # Entrada da Batata Frita (sem tratamento de erro, para simplificar)
        q_batata_str = input(f"Quantidade de Batatas Fritas (R$ {batata_preco:.2f}): ")
        q_batata = int(q_batata_str)

        # Entrada do Refrigerante (sem tratamento de erro)
        q_refrigerante_str = input(f"Quantidade de Refrigerantes (R$ {refrigerante_preco:.2f}): ")
        q_refrigerante = int(q_refrigerante_str)

        # Garante que as quantidades não são negativas (boa prática)
        if q_hamburguer < 0 or q_batata < 0 or q_refrigerante < 0:
            print("Aviso: Quantidade negativa não permitida. Usando 0 para quantidades inválidas.")
            q_hamburguer = max(0, q_hamburguer)
            q_batata = max(0, q_batata)
            q_refrigerante = max(0, q_refrigerante)

        # === 3. Cálculo do Total ===
        preco_total = (hamburguer_preco * q_hamburguer) + \
                      (batata_preco * q_batata) + \
                      (refrigerante_preco * q_refrigerante)

        # === 4. Saída de Dados: Exibição do Resultado ===
        print("-" * 40)
        print("CÁLCULO FINALIZADO")

        # Exibe o total formatado como moeda (duas casas decimais)
        print(f"O preço total do seu pedido é: R$ {preco_total:.2f}")
        print("=" * 40)

    # Captura erro se o primeiro item (hambúrguer) não for um número
    except ValueError:
        print("\nERRO DE ENTRADA: Você deve digitar um número inteiro para a quantidade.")
        print("O cálculo foi interrompido.")

    except Exception as e:
        print(f"\nERRO INESPERADO: Ocorreu um erro: {e}")


# Executa o programa
calcular_compra_variaveis()