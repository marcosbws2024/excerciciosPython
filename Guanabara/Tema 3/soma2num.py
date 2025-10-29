import sys

def soma_numeros_segura():
    print("--- Calculadora de Soma ---")

    try:
        # As linhas dentro do TRY devem ser indentadas
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        soma = num1 + num2

        print(f"A soma dos números é: {soma}")

    # 🚨 Tratamento de Erros Comuns:

    # 1. Captura a exceção gerada por Ctrl+C (interrupção do teclado)
    except KeyboardInterrupt:
        # O bloco EXCEPT deve ser indentado
        print("\n\n--- Interrompido pelo usuário. ---")
        sys.exit(0)

    # 2. Captura qualquer outro erro, como ValueError (se digitar texto)
    except Exception as e:
        # A linha de erro deve ser indentada
        print(f"\n--- Erro! ---")
        print(f"Ocorreu um erro: {e}")
        print("Certifique-se de digitar apenas números inteiros.")


# Executa a função
soma_numeros_segura()
