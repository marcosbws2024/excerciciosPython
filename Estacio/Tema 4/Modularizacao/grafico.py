from tkinter import * ## 1. DEFINIÇÃO DA FUNÇÃO (DEVE VIR PRIMEIRO)
def funcClicar():
    # Esta função será chamada quando o botão for clicado
    print("O botão foi clicado! A função está funcionando.")
    # Você pode mudar o texto do Label aqui, se quiser:
    texto.config(text="CLICADO!")
    return 0

## 2. CONFIGURAÇÃO DA INTERFACE
JanelaPrincipal = Tk()
JanelaPrincipal.title("Janela Tkinter")
JanelaPrincipal.geometry("300x200") # Define um tamanho para visualizar

# Label
texto = Label(master = JanelaPrincipal, text = "Minha Janela Principal")
# Pack é geralmente suficiente, mas se usar place, remova o pack()
texto.pack() 

# Botão
# A função 'funcClicar' JÁ EXISTE neste ponto.
botao = Button(master = JanelaPrincipal, text = 'clique', command= funcClicar)
botao.pack()

# Nota: Você usou .pack() e .place() para 'texto'. 
# Use apenas um por widget. O 'pack()' será aplicado primeiro e o 'place()' vai substituí-lo.

# texto.place(x=50, y=100) # Se quiser usar place, remova o texto.pack() acima

# Inicia o loop principal da interface
JanelaPrincipal.mainloop()





