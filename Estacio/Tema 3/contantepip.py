from enum import Enum

# Define a classe de constantes
class ConstantesMatematicas(Enum):
    # Membros do Enum são constantes e imutáveis
    PI = 3.14159
    GRAVIDADE = 9.80665

# Acesso aos valores (usando .value)
raio = 5
area = ConstantesMatematicas.PI.value * (raio ** 2)

print(f"PI: {ConstantesMatematicas.PI.value}")
print(f"Area do Circulo: {area}")

# Tentar alterar uma constante do Enum causa um erro
try:
    ConstantesMatematicas.PI.value = 3.0
except AttributeError as e:
    print(f"\nSucesso! Constante não pôde ser alterada: {e}")