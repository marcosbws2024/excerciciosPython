import tkinter as tk
from tkinter import messagebox

# --- FUNÇÃO DE CADASTRO (Apenas simulação) ---
def cadastrar_cliente():
    """Simula o processamento dos dados do formulário."""
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    
    if nome and email and telefone:
        messagebox.showinfo(
            "Cadastro Realizado",
            f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\n\nDados prontos para envio ao BD!"
        )
        # Limpar campos após o cadastro simulado
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# --- CONFIGURAÇÃO DA INTERFACE TKINTER ---

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Cadastro de Cliente Responsivo")

# 1. Torna a coluna central (coluna 1) expansível. 
# Isso é fundamental para a responsividade: o campo de entrada expandirá 
# junto com a janela.
janelaPrincipal.grid_columnconfigure(1, weight=1)

# 2. Cria um Frame para agrupar os widgets e aplicar padding de forma limpa.
frame_cadastro = tk.Frame(janelaPrincipal, padx=10, pady=10)
frame_cadastro.grid(row=0, column=0, sticky="nsew") 
# O frame deve se expandir com a janela, por isso usamos sticky="nsew"

# Torna a coluna 1 DENTRO do frame expansível também
frame_cadastro.grid_columnconfigure(1, weight=1)

# --- WIDGETS DE CADASTRO ---

# 1. Campo NOME
label_nome = tk.Label(frame_cadastro, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w") # Alinha à esquerda (west)
entry_nome = tk.Entry(frame_cadastro, width=40)
# 'sticky="ew"' faz o campo de entrada preencher o espaço da célula (east-west)
entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="ew") 

# 2. Campo E-MAIL
label_email = tk.Label(frame_cadastro, text="E-mail:")
label_email.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_email = tk.Entry(frame_cadastro, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# 3. Campo TELEFONE
label_telefone = tk.Label(frame_cadastro, text="Telefone:")
label_telefone.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_telefone = tk.Entry(frame_cadastro, width=40)
entry_telefone.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# 4. Botão de Cadastro
botao_cadastrar = tk.Button(frame_cadastro, text="Cadastrar Cliente", command=cadastrar_cliente)
# 'columnspan=2' faz o botão ocupar as duas colunas
botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=15) 

# Inicia o loop principal da interface
janelaPrincipal.mainloop()