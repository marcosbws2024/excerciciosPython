import tkinter as tk 
from tkinter import ttk 
from AppBD import BancoDados
 
class BibliotecaGUI: 
       def __init__(self, root, bd): 
           self.bd = bd 
           self.root = root 
           self.root.title("Gerenciador de Biblioteca") 
            
           self.tree = ttk.Treeview(root, columns=("ID", "Título", "Autor", "Ano", "Gênero"), show="headings") 
           self.tree.heading("ID", text="ID") 
           self.tree.heading("Título", text="Título") 
           self.tree.heading("Autor", text="Autor") 
           self.tree.heading("Ano", text="Ano de Publicação") 
           self.tree.heading("Gênero", text="Gênero") 
           self.tree.pack() 
 
           self.carregar_dados() 
 
       def carregar_dados(self): 
           registros = self.bd.selecionar_dados() 
           for registro in registros: 
               self.tree.insert("", "end", values=registro) 
 
root = tk.Tk() 
app_bd = BancoDados() 
app_gui = BibliotecaGUI(root, app_bd) 
root.mainloop() 
  