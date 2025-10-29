"""preco_arroz = 10.00
preco_feijao = 8.50
preco_macarrao = 5.25

quantidade_arroz = int(input("Digite a quantidade de pacotes de arroz: "))
quantidade_feijao = int(input("Digite a quantidade de pacotes de feijão: "))
quantidade_macarrao = int(input("Digite a quantidade de pacotes de macarrão: "))


total_compra = (preco_arroz * quantidade_arroz) + (preco_feijao * quantidade_feijao) + (preco_macarrao * quantidade_macarrao)
print("O total da sua compra é: R$", total_compra)"""

import sys


def calcular_compra_permite_zero():
    # Definição dos Preços
    preco_arroz = 10.00
    preco_feijao = 8.50
    preco_macarrao = 5.25

    print("--- Cálculo do Total da Compra ---")
    print(" (Pressione ENTER ou digite 0 se não quiser o item. CTRL+C para sair.)")

    try:
        # --- 1. ENTRADA DE DADOS E CONVERSÃO ---

        # O padrão: se a entrada estiver vazia, a quantidade será 0. Caso contrário, tenta converter.

        # ARROZ
        entrada_arroz = input("Digite a quantidade de pacotes de arroz: ").strip()
        # Se a string estiver vazia (''), quantidade_arroz será 0. Senão, tenta int().
        quantidade_arroz = int(entrada_arroz) if entrada_arroz else 0

        # FEIJÃO
        entrada_feijao = input("Digite a quantidade de pacotes de feijão: ").strip()
        quantidade_feijao = int(entrada_feijao) if entrada_feijao else 0

        # MACARRÃO
        entrada_macarrao = input("Digite a quantidade de pacotes de macarrão: ").strip()
        quantidade_macarrao = int(entrada_macarrao) if entrada_macarrao else 0

        # --- 2. VALIDAÇÃO DE NEGATIVOS (Única restrição) ---

        # A única validação de erro de lógica que mantemos é para números negativos.
        if quantidade_arroz < 0 or quantidade_feijao < 0 or quantidade_macarrao < 0:
            raise ValueError("As quantidades digitadas não podem ser negativas.")

        # --- 3. CÁLCULO DO TOTAL ---
        total_compra = (preco_arroz * quantidade_arroz) + \
                       (preco_feijao * quantidade_feijao) + \
                       (preco_macarrao * quantidade_macarrao)

        # --- 4. SAÍDA DE SUCESSO ---
        print("-" * 35)
        print(f"O total da sua compra é: R$ {total_compra:.2f}")
        print("Programa finalizado.")
        print("-" * 35)

    # 🚨 TRATAMENTO DE INTERRUPÇÃO (Ctrl + C) 🚨
    except KeyboardInterrupt:
        print("\n\n--- Interrupção detectada! Programa encerrado de forma limpa. ---")
        sys.exit(0)

        # 🚨 TRATAMENTO DE ERROS DE VALOR (Texto ou Negativo) 🚨
    except ValueError as e:
        print("-" * 35)
        # Este except pega: texto, ponto decimal (float), ou a exceção que levantamos (negativos).
        print(f"ERRO DE VALIDAÇÃO: {e}")
        print("Por favor, digite um número inteiro (0 ou maior).")
        print("O cálculo não pôde ser realizado.")
        print("-" * 35)

    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")


# Executa a função
calcular_compra_permite_zero()