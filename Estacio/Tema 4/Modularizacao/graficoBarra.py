import numpy as np
import matplotlib.pyplot as plt

# --- 1. Preparação dos Dados ---
# Categoria (Eixo X) - Criado como array NumPy
categorias = np.array(['A', 'B', 'C', 'D']) 
# Valores (Eixo Y - Altura das Barras) - Criado como array NumPy
valores = np.array([3, 8, 1, 10]) 

# --- 2. Criação da Visualização ---
# Define a cor das barras (opcional: 'skyblue', 'green', 'red', etc.)
cor_barra = 'teal' 

# Cria o gráfico de barras
plt.bar(categorias, valores, color=cor_barra)

# --- 3. Personalização (Rótulos e Título) ---
plt.title('Distribuição de Valores por Categoria', fontsize=14, fontweight='bold')
plt.xlabel('Categorias (Rótulos no Eixo X)', fontsize=12)
plt.ylabel('Valores (Magnitude)', fontsize=12)

# Adiciona uma grade horizontal sutil para facilitar a leitura dos valores
plt.grid(axis='y', linestyle='--', alpha=0.7)

# --- 4. Exibição ---
# Garante que o layout se ajuste bem aos rótulos
plt.tight_layout()
# Exibe a janela do gráfico
plt.show()