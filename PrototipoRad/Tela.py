import tkinter as tk
from tkinter import messagebox

class SaborRapidoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x650") # Aumentei um pouco a altura para caber tudo

        self.itens_menu = {"Hambúrguer": 10.00, "Batata Frita": 5.00, "Refrigerante": 3.00}
        self.pedido = []

        # --- SEÇÃO DE SELEÇÃO DE PEDIDO ---
        tk.Label(root, text="Selecione os itens do pedido:", font=("Arial", 12, "bold")).pack(pady=10)
        
        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.listbox.pack(fill=tk.X, padx=20)
        self.atualizar_lista_menu()

        tk.Button(root, text="Adicionar ao Pedido", command=self.adicionar_pedido, bg="#d1e7dd").pack(pady=5)
        tk.Button(root, text="Visualizar Pedido", command=self.visualizar_pedido).pack(pady=5)
        tk.Button(root, text="Finalizar Pedido", command=self.finalizar_pedido, bg="#f8d7da").pack(pady=5)

        # Linha divisória visual
        tk.Canvas(root, height=2, bg="gray", bd=0, highlightthickness=0).pack(fill=tk.X, padx=20, pady=20)

        # --- SEÇÃO DE CADASTRO DE NOVOS PRODUTOS ---
        tk.Label(root, text="Adicionar Novo Item ao Menu:", font=("Arial", 12, "bold")).pack(pady=10)
        
        tk.Label(root, text="Nome do Produto:").pack()
        self.entry_item = tk.Entry(root, font=("Arial", 10))
        self.entry_item.pack(pady=2)
        
        tk.Label(root, text="Preço (Ex: 15.50):").pack()
        self.entry_preco = tk.Entry(root, font=("Arial", 10))
        self.entry_preco.pack(pady=2)
        
        tk.Button(root, text="Cadastrar no Menu", command=self.adicionar_item_menu, bg="#fff3cd").pack(pady=10)

    def atualizar_lista_menu(self):
        self.listbox.delete(0, tk.END)
        for item, preco in self.itens_menu.items():
            self.listbox.insert(tk.END, f"{item} - R$ {preco:.2f}")

    def adicionar_pedido(self):
        selecionados = self.listbox.curselection()
        if not selecionados:
            messagebox.showwarning("Atenção", "Selecione ao menos um item da lista.")
            return
            
        for index in selecionados:
            # Pegamos apenas o nome do item antes do traço " - "
            texto_item = self.listbox.get(index)
            nome_item = texto_item.split(" - ")[0]
            self.pedido.append(nome_item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedido(self):
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido.")
            return
        pedido_texto = "\n".join(self.pedido)
        messagebox.showinfo("Pedido Atual", f"Itens no pedido:\n{pedido_texto}")

    def finalizar_pedido(self):
        if not self.pedido:
            messagebox.showwarning("Erro", "Adicione itens antes de finalizar.")
            return
        
        total = sum(self.itens_menu[item] for item in self.pedido)
        messagebox.showinfo("Total", f"Total do pedido: R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()

    def adicionar_item_menu(self):
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        
        if item and preco:
            try:
                # Substitui vírgula por ponto caso o usuário digite no padrão brasileiro
                preco_limpo = float(preco.replace(',', '.'))
                self.itens_menu[item] = preco_limpo
                self.atualizar_lista_menu()
                
                # Limpa os campos após adicionar
                self.entry_item.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                messagebox.showinfo("Sucesso", f"'{item}' adicionado ao cardápio!")
            except ValueError:
                messagebox.showerror("Erro", "Preço inválido. Use números (ex: 10.50).")
        else:
            messagebox.showwarning("Atenção", "Preencha o nome e o preço do produto.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()