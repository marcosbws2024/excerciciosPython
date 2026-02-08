import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Exemplo Simples")
        self.geometry("400x300")

        # Configuração de campos (Equivalente ao ControlText)
        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=(10, 0))
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.insert(0, "João")
        self.entry_nome.pack(pady=5)

        self.label_sobrenome = ctk.CTkLabel(self, text="Sobrenome:")
        self.label_sobrenome.pack(pady=(10, 0))
        self.entry_sobrenome = ctk.CTkEntry(self)
        self.entry_sobrenome.insert(0, "Silva")
        self.entry_sobrenome.pack(pady=5)

        # Botão (Equivalente ao ControlButton)
        self.button = ctk.CTkButton(self, text="Gerar Nome Completo", command=self.gerar_nome)
        self.button.pack(pady=20)

        # Campo de Resultado
        self.entry_completo = ctk.CTkEntry(self, width=300)
        self.entry_completo.pack(pady=10)

    def gerar_nome(self):
        nome_completo = f"{self.entry_nome.get()} {self.entry_sobrenome.get()}"
        self.entry_completo.delete(0, "end")
        self.entry_completo.insert(0, nome_completo)

if __name__ == "__main__":
    app = App()
    app.mainloop()