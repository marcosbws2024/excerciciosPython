a = int(input("Digite um valor inteiro:"))
b = float(input("Digite um valor float:"))

# --- AQUI ESTÁ A SOLUÇÃO CORRETA ---
entrada_c = input("Digite um Valor Booleano (True/False):").strip().lower()

# Verifica se a string digitada é "true" ou "1" para ser True, caso contrário é False.
# Nota: 'false', '0', ou qualquer outra coisa será False
if entrada_c in ('true', '1', 'sim'):
    c = True
elif entrada_c in ('false', '0', 'nao', 'não'):
    c = False
else:
    # Tratar entradas inválidas, opcionalmente
    print(f"Aviso: Entrada '{entrada_c}' não reconhecida. Definition como False.")
    c = False
# ------------------------------------

print(f"\n--- Resultados da Conversão ---")
print(f"Numero Inteiro: {a} (tipo: {type(a).__name__})")
print(f"Numero Float: {b} (tipo: {type(b).__name__})")
print(f"Valor booleano: {c} (tipo: {type(c).__name__})")

#numero_inteiro = int(input("Digite um número inteiro: "))
#numero_flutuante = float(input("Digite um número de ponto flutuante: "))
#valor_booleano = input("Digite um valor booleano (True ou False): ")
#valor_booleano = valor_booleano.lower()  # Converte para minúsculas para garantir que seja reconhecido como booleano
#valor_booleano = valor_booleano == "true"  # Converte para tipo bool

#print("\nValores convertidos:")
#print(f"- Número inteiro: {numero_inteiro} (tipo: {type(numero_inteiro).__name__})")
#print(f"- Número de ponto flutuante: {numero_flutuante} (tipo: {type(numero_flutuante).__name__})")
#print(f"- Valor booleano: {valor_booleano} (tipo: {type(valor_booleano).__name__})")
