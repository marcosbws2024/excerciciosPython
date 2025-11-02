listaPeso = [] 
NUMERO_DE_PESSOAS = 5

for i in range(NUMERO_DE_PESSOAS):
    try:
        peso = float(input(f"Peso da Pessoa {i + 1}: "))
        listaPeso.append(peso)
    except ValueError:
        print("Entrada inválida. Digite um número.")

if listaPeso:
    print(f"\nMAIOR peso: {max(listaPeso):.2f} kg")
    print(f"MENOR peso: {min(listaPeso):.2f} kg")