def minha_funcao(msg): # CORREÇÃO 1: Adicionado ":"
    print(msg)

    if True: # CORREÇÃO 2: Adicionado ":"
        print("Condição verdadeira") # CORREÇÃO 3: Indentação correta para o if

# --- Bloco Principal (Corrigido para evitar erro de divisão por zero) ---
try:
    n = 0
    # A divisão por zero será tratada
    resultado = 10 / n 
    
    # Esta linha só seria executada se a divisão fosse bem-sucedida
    minha_funcao(resultado) 
    
except ZeroDivisionError:
    print("\nERRO: Não é possível dividir por zero (ZeroDivisionError).")
    # Para o programa continuar, podemos chamar a função com uma mensagem alternativa
    minha_funcao("Divisão por zero detectada e tratada.")

# CORREÇÃO 5: A chamada da função deve estar sem indentação se for no bloco principal.
# (Se fosse para rodar o resultado, estaria dentro do 'try' acima).