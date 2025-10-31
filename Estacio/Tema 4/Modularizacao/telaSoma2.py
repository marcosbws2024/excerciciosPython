import tkinter as tk
from tkinter import messagebox

# --- FUNÇÃO DE CÁLCULO CORRIGIDA ---
def somarNumeros():
    """Realiza a soma dos números inseridos nos campos de entrada."""
    try:
        # CORREÇÃO 1: Usar entry_num1 e entry_num2 para obter os dois valores
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get()) # <-- CORRIGIDO AQUI
        
        resultado = num1 + num2
        
        # CORREÇÃO 2: A função correta é showinfo
        messagebox.showinfo("Resultado", f"A soma dos números é: {resultado}")
        
    except ValueError:
        # Captura erros se o usuário digitar algo que não é um número
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números válidos.")
    
    # CORREÇÃO 3 e 4: REMOVIDAS as linhas 'janela = tk.Tk()' e 'janela.titlle()'
    # A janela principal (root) já está criada e não deve ser recriada aqui.


# --- CONFIGURAÇÃO DA INTERFACE TKINTER ---

# CORREÇÃO 3: A janela principal é criada APENAS UMA VEZ no início
janela = tk.Tk()  
# CORREÇÃO 4: O método correto é 'title'
janela.title("Calculadora de Soma") 

# 1. Campo de Entrada para o Primeiro Número (num1)
label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# 2. Campo de Entrada para o Segundo Número (num2)
label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_num2 = tk.Entry(janela) # Esta variável estava faltando no seu código
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# 3. Botão para Chamar a Função de Soma
botao_somar = tk.Button(janela, text="Somar", command=somarNumeros)
botao_somar.grid(row=2, column=0, columnspan=2, pady=10)


janela.mainloop()