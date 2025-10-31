import tkinter as tk
from datetime import datetime
import time 

# --- FUNÇÃO DE ATUALIZAÇÃO DO RELÓGIO ---
def atualizar_relogio():
    """Obtém a hora atual e a exibe no Label."""
    
    # 1. Obtém o tempo atual
    # strftime formata a data/hora: %H=Hora, %M=Minuto, %S=Segundo
    hora_atual = datetime.now().strftime("%H:%M:%S")
    
    # 2. Atualiza o texto do Label
    label_relogio.config(text=hora_atual)
    
    # 3. Agenda a próxima execução
    # O método 'after' espera 1000 milissegundos (1 segundo) e chama a função novamente.
    janela_principal.after(1000, atualizar_relogio)

# --- CONFIGURAÇÃO DA INTERFACE TKINTER ---

janela_principal = tk.Tk()
janela_principal.title("Relógio Digital")

# 1. Cria um Label para exibir a hora (fonte maior para destaque)
label_relogio = tk.Label(
    janela_principal, 
    text="00:00:00", 
    font=('Helvetica', 48), 
    bg='black', 
    fg='white'
)
label_relogio.pack(pady=50, padx=50)

# 2. Inicia o processo de atualização do relógio
atualizar_relogio()

# 3. Inicia o loop principal da interface
janela_principal.mainloop()