import tkinter as tk

def criar_tela_grid_responsiva():
    janela = tk.Tk()
    janela.title("Layout Grid Responsivo")
    
    # 1. TORNAR A COLUNA 1 RESPONSIVA
    # O 'weight=1' faz com que a coluna 1 (onde estão os campos Entry)
    # receba todo o espaço extra quando a janela for redimensionada.
    janela.grid_columnconfigure(1, weight=1)
    
    # Widgets
    
    # NOME
    label_nome = tk.Label(janela, text="Nome:")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w") # 'w' = Alinha à esquerda
    
    entry_nome = tk.Entry(janela, width=30)
    # 'sticky="ew"' faz o campo de entrada preencher o espaço da célula (East-West)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew") 
    
    # E-MAIL
    label_email = tk.Label(janela, text="E-mail:")
    label_email.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    entry_email = tk.Entry(janela, width=30)
    entry_email.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
    
    # BOTÃO
    botao_salvar = tk.Button(janela, text="Salvar Cadastro")
    # 'columnspan=2' faz o botão ocupar as duas colunas
    botao_salvar.grid(row=2, column=0, columnspan=2, pady=15)
    
    janela.mainloop()

# criar_tela_grid_responsiva()