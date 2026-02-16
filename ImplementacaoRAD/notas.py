import tkinter as tk
from tkinter import ttk, messagebox

class GestaoEscolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Escolar")
        self.root.geometry("750x500")

        # --- Frame de Entrada de Dados ---
        self.frame_campos = tk.LabelFrame(root, text="Cadastro de Aluno", padx=10, pady=10)
        self.frame_campos.pack(pady=10, padx=10, fill="x")

        tk.Label(self.frame_campos, text="Nome:").grid(row=0, column=0, sticky="e")
        self.ent_nome = tk.Entry(self.frame_campos)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(self.frame_campos, text="Nota 1:").grid(row=0, column=2, sticky="e")
        self.ent_nota1 = tk.Entry(self.frame_campos, width=10)
        self.ent_nota1.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(self.frame_campos, text="Nota 2:").grid(row=0, column=4, sticky="e")
        self.ent_nota2 = tk.Entry(self.frame_campos, width=10)
        self.ent_nota2.grid(row=0, column=5, padx=5, pady=2)

        self.btn_cadastrar = tk.Button(self.frame_campos, text="Cadastrar Aluno", 
                                       command=self.cadastrar_aluno, bg="#4CAF50", fg="white")
        self.btn_cadastrar.grid(row=0, column=6, padx=10)

        # --- Tabela (Treeview) ---
        self.tabela = ttk.Treeview(root, columns=("Nome", "Nota1", "Nota2", "Média", "Situação"), show="headings")
        self.tabela.heading("Nome", text="Nome do Aluno")
        self.tabela.heading("Nota1", text="Nota 1")
        self.tabela.heading("Nota2", text="Nota 2")
        self.tabela.heading("Média", text="Média")
        self.tabela.heading("Situação", text="Situação")
        
        # Estilizando colunas
        self.tabela.column("Nome", width=200)
        self.tabela.column("Nota1", width=80, anchor="center")
        self.tabela.column("Nota2", width=80, anchor="center")
        self.tabela.column("Média", width=80, anchor="center")
        self.tabela.column("Situação", width=120, anchor="center")
        
        self.tabela.pack(pady=10, padx=10, fill="both", expand=True)

        self.carregar_iniciais()

    def calcular_situacao(self, media):
        if media >= 7: return "Aprovado"
        if media >= 5: return "Recuperação"
        return "Reprovado"

    def cadastrar_aluno(self):
        try:
            nome = self.ent_nome.get()
            n1 = float(self.ent_nota1.get())
            n2 = float(self.ent_nota2.get())
            
            if not nome:
                raise ValueError("O nome é obrigatório")

            media = (n1 + n2) / 2
            situacao = self.calcular_situacao(media)

            self.tabela.insert("", "end", values=(nome, n1, n2, f"{media:.2f}", situacao))
            
            # Limpar campos após sucesso
            self.ent_nome.delete(0, tk.END)
            self.ent_nota1.delete(0, tk.END)
            self.ent_nota2.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro de Entrada", "Preencha os campos corretamente (Use ponto em vez de vírgula nas notas)")

    def carregar_iniciais(self):
        alunos = [("Alice", 8.5, 7.0), ("Bruno", 5.0, 6.0), ("Carlos", 3.5, 4.0)]
        for nome, n1, n2 in alunos:
            m = (n1 + n2) / 2
            s = self.calcular_situacao(m)
            self.tabela.insert("", "end", values=(nome, n1, n2, f"{m:.2f}", s))

if __name__ == "__main__":
    root = tk.Tk()
    app = GestaoEscolar(root)
    root.mainloop()