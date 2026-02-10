import tkinter as tk
from tkinter import ttk, messagebox
from AppBD import BancoDados

class BibliotecaGUI:
    def __init__(self, root, bd):
        self.bd = bd
        self.root = root
        self.root.title("Gerenciador de Biblioteca - CRUD Completo")
        self.root.geometry("700x500")

        # --- 1. CAMPOS DE ENTRADA (Inputs) ---
        frame_inputs = tk.LabelFrame(root, text="Dados do Livro", padx=10, pady=10)
        frame_inputs.pack(pady=10, fill="x", padx=10)

        tk.Label(frame_inputs, text="Título:").grid(row=0, column=0, sticky="e")
        self.ent_titulo = tk.Entry(frame_inputs, width=30)
        self.ent_titulo.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_inputs, text="Autor:").grid(row=0, column=2, sticky="e")
        self.ent_autor = tk.Entry(frame_inputs, width=30)
        self.ent_autor.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_inputs, text="Ano:").grid(row=1, column=0, sticky="e")
        self.ent_ano = tk.Entry(frame_inputs, width=30)
        self.ent_ano.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_inputs, text="Gênero:").grid(row=1, column=2, sticky="e")
        self.ent_genero = tk.Entry(frame_inputs, width=30)
        self.ent_genero.grid(row=1, column=3, padx=5, pady=2)

        # --- 2. BOTÕES ---
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Adicionar Novo", command=self.f_inserir, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Salvar Alterações", command=self.f_atualizar, bg="blue", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Excluir Livro", command=self.f_excluir, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Limpar Campos", command=self.limpar_campos).pack(side=tk.LEFT, padx=5)

        # --- 3. TABELA (Treeview) ---
        self.tree = ttk.Treeview(root, columns=("ID", "Título", "Autor", "Ano", "Gênero"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Ano", text="Ano")
        self.tree.heading("Gênero", text="Gênero")
        
        # Ajustando largura das colunas
        self.tree.column("ID", width=50)
        self.tree.column("Título", width=200)
        
        # Evento: quando clicar na linha, preenche os campos acima
        self.tree.bind("<<TreeviewSelect>>", self.preencher_campos)
        self.tree.pack(pady=10, fill="both", expand=True)

        self.carregar_dados()

    # --- LÓGICA ---

    def carregar_dados(self):
        # Limpa a tabela antes de recarregar
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Busca no AppBD
        for registro in self.bd.selecionar_dados():
            self.tree.insert("", "end", values=registro)

    def f_inserir(self):
        if self.ent_titulo.get() == "":
            messagebox.showwarning("Erro", "O título é obrigatório!")
            return
        self.bd.inserir_dados(self.ent_titulo.get(), self.ent_autor.get(), self.ent_ano.get(), self.ent_genero.get())
        self.carregar_dados()
        self.limpar_campos()

    def f_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um livro na tabela para editar")
            return
        
        id_livro = self.tree.item(selecionado)['values'][0]
        self.bd.atualizar_dado(id_livro, self.ent_titulo.get(), self.ent_autor.get(), self.ent_ano.get(), self.ent_genero.get())
        self.carregar_dados()
        messagebox.showinfo("Sucesso", "Livro atualizado!")

    def f_excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um livro para excluir")
            return
        
        if messagebox.askyesno("Confirmar", "Deseja realmente excluir este livro?"):
            id_livro = self.tree.item(selecionado)['values'][0]
            self.bd.deletar_dado(id_livro)
            self.carregar_dados()
            self.limpar_campos()

    def preencher_campos(self, event):
        selecionado = self.tree.selection()
        if selecionado:
            valores = self.tree.item(selecionado)['values']
            self.limpar_campos()
            self.ent_titulo.insert(0, valores[1])
            self.ent_autor.insert(0, valores[2])
            self.ent_ano.insert(0, valores[3])
            self.ent_genero.insert(0, valores[4])

    def limpar_campos(self):
        self.ent_titulo.delete(0, tk.END)
        self.ent_autor.delete(0, tk.END)
        self.ent_ano.delete(0, tk.END)
        self.ent_genero.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app_bd = BancoDados()
    app_gui = BibliotecaGUI(root, app_bd)
    root.mainloop()