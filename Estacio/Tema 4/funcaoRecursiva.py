def regressiva(x):
   if x <= 0:
    print("Acabou")
   else:
    print(x)
    regressiva(x-1)

def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)

#nao recursiva
def fatorial1(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
           fat = fat*x
        return fat

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo1(n):
    'Determina o n-ésimo termo da sequência de Fibonacci de forma recursiva.'

    # Verificação de casos base: 1º e 2º termo são iguais a 1.
    if n == 1 or n == 2:
        return 1

    # Verificação de entrada inválida (opcional, mas recomendado)
    if n <= 0:
        raise ValueError("O termo 'n' deve ser um número inteiro positivo.")

    # Passo recursivo: A soma dos dois termos anteriores
    else:
        # Chamada correta: fibo1 e subtração (n - 2)
        return fibo1(n - 1) + fibo1(n - 2)


# --- 1. Imprimindo a Ajuda (Docstring) ---
# Usamos help() para exibir a string de documentação (docstring) de fibo1.
print("--- Saída de help(fibo1) ---")
help(fibo1)
