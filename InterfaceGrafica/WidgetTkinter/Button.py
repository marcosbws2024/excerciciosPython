import tkinter as tk

contador = 0

def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        # O after agenda a próxima execução para daqui a 1000ms (1 segundo)
        lblRotulo.after(1000, funcao_contar)
    
    # Chamamos a função pela primeira vez (FORA da definição interna)
    funcao_contar()

janela = tk.Tk()
janela.title("Contagem dos Segundos")
janela.geometry("400x150") # Definindo um tamanho para a janela

lblRotulo = tk.Label(janela, fg="green", font=("Helvetica", 30, "bold"))
lblRotulo.pack(pady=20)

# Inicia a lógica da contagem
contador_label(lblRotulo)

btnAcao = tk.Button(janela, 
                    text='Clique aqui para Interromper a contagem', 
                    width=40, 
                    command=janela.destroy)
btnAcao.pack(pady=10)

janela.mainloop()