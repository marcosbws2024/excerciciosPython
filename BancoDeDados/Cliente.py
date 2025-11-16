# app_tela.py

import tkinter as tk
from tkinter import ttk, messagebox

# Importa as classes de outros módulos
from Classes.Conexao import Conexao 
from Classes.ClienteDao import ClienteDao

class Tela:
    """Interface gráfica Tkinter para cadastro e gestão de clientes, com busca dinâmica."""
    
    def __init__(self, master, cliente_dao):
        self.master = master
        self.master.title("Cadastro e Gestão de Clientes")
        self.cliente_dao = cliente_dao
        
        # Variáveis de Estado
        self.tree = None 
        self.dados_clientes = [] 
        self.search_entry = None 
        
        # Elementos da GUI
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")
        
        # Variáveis de Entry
        self.id_entry = self.nome_update_entry = self.email_update_entry = None
        self.nome_entry = self.email_entry = self.telefone_entry = None
        
        # Criação das abas (Índices: 0, 1, 2)
        self._create_register_tab()
        self._create_update_delete_tab()
        self._create_list_tab() 

        # BIND: Carregamento Automático ao mudar de aba
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_change)

    # --- Métodos de Criação das Abas (Omitidos para brevidade, pois não mudaram) ---
    def _create_register_tab(self):
        tab_cadastro = ttk.Frame(self.notebook)
        self.notebook.add(tab_cadastro, text=" ➕ Cadastrar ")
        
        ttk.Label(tab_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.nome_entry = ttk.Entry(tab_cadastro, width=40)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(tab_cadastro, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ttk.Entry(tab_cadastro, width=40)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(tab_cadastro, text="Telefone:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.telefone_entry = ttk.Entry(tab_cadastro, width=40)
        self.telefone_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(tab_cadastro, text="✔️ Cadastrar", command=self._handle_cadastro).grid(row=3, columnspan=2, pady=10)

    def _create_update_delete_tab(self):
        tab_gerenciar = ttk.Frame(self.notebook)
        self.notebook.add(tab_gerenciar, text=" 🔄 Gerenciar/Deletar ")
        
        ttk.Label(tab_gerenciar, text="ID Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.id_entry = ttk.Entry(tab_gerenciar, width=10)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(tab_gerenciar, text="Novo Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.nome_update_entry = ttk.Entry(tab_gerenciar, width=40)
        self.nome_update_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(tab_gerenciar, text="Novo Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_update_entry = ttk.Entry(tab_gerenciar, width=40)
        self.email_update_entry.grid(row=2, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(tab_gerenciar)
        btn_frame.grid(row=3, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="✏️ Atualizar", command=self._handle_atualizar).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="❌ Deletar", command=self._handle_deletar).pack(side="left", padx=10)

    def _create_list_tab(self):
        tab_listagem = ttk.Frame(self.notebook)
        self.notebook.add(tab_listagem, text=" 📋 Listar Clientes ")
        
        # Frame de Busca
        search_frame = ttk.Frame(tab_listagem)
        search_frame.pack(pady=10, padx=10, fill="x")
        
        ttk.Label(search_frame, text="Buscar:").pack(side="left", padx=5)
        self.search_entry = ttk.Entry(search_frame, width=50)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        self.search_entry.bind("<KeyRelease>", self._filtrar_dados_clientes) 
        
        ttk.Button(search_frame, text="Recarregar DB", command=self._carregar_dados_clientes).pack(side="left", padx=5)

        # Configuração do Treeview (Tabela)
        self.tree = ttk.Treeview(tab_listagem, columns=("ID", "Nome", "Email", "Telefone"), show="headings")
        
        col_settings = {
            "ID": (40, tk.CENTER), "Nome": (150, tk.W), 
            "Email": (200, tk.W), "Telefone": (100, tk.W)
        }
        for col, (width, anchor) in col_settings.items():
            self.tree.heading(col, text=col.replace("ID", "ID Cliente"))
            self.tree.column(col, width=width, anchor=anchor)

        scrollbar = ttk.Scrollbar(tab_listagem, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tree.pack(padx=10, pady=10, expand=True, fill="both")

        self.tree.bind("<Double-1>", self._on_double_click_tree) 

    # --- Lógica de Limpeza de Campos (NOVA FUNÇÃO) ---

    def _limpar_campos_cadastro_e_gerenciamento(self, aba_limpar):
        """
        Limpa os campos de Entry nas abas de Cadastro ou Gerenciamento.
        :param aba_limpar: 'cadastro' ou 'gerenciamento'.
        """
        if aba_limpar == 'cadastro':
            # Limpa campos da aba Cadastrar
            self.nome_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
        
        elif aba_limpar == 'gerenciamento':
            # Limpa campos da aba Gerenciar/Deletar
            self.id_entry.delete(0, tk.END)
            self.nome_update_entry.delete(0, tk.END)
            self.email_update_entry.delete(0, tk.END)

    # --- Lógica de Eventos e Consulta (Mantida) ---

    def _on_tab_change(self, event):
        """Carrega os dados do DB quando a aba de listagem (índice 2) é selecionada."""
        if self.notebook.index(self.notebook.select()) == 2:
            self._carregar_dados_clientes()

    def _carregar_dados_clientes(self):
        """Busca os dados do DB, ARMAZENA na memória e aciona o filtro."""
        self.tree.delete(*self.tree.get_children())
        self.dados_clientes = [] 
        
        clientes = self.cliente_dao.buscar_todos_clientes()
        
        if clientes:
            self.dados_clientes = clientes
            
        self._filtrar_dados_clientes()

    def _filtrar_dados_clientes(self, event=None):
        """Filtra os dados armazenados em self.dados_clientes e atualiza o Treeview."""
        self.tree.delete(*self.tree.get_children())
        
        termo_busca = self.search_entry.get().lower()
        dados_filtrados = []
        
        if not termo_busca:
            dados_filtrados = self.dados_clientes
        else:
            for cliente in self.dados_clientes:
                cliente_str = [str(x).lower() for x in cliente] 
                if any(termo_busca in campo for campo in cliente_str):
                    dados_filtrados.append(cliente)

        for cliente in dados_filtrados:
            self.tree.insert("", tk.END, values=cliente)

    def _on_double_click_tree(self, event):
        """Preenche os campos de gerenciamento com os dados da linha clicada."""
        item_id = self.tree.focus()
        if not item_id: return

        valores = self.tree.item(item_id, 'values')
        if not valores: return

        self.notebook.select(1) # Mudar para aba Gerenciar/Deletar

        cliente_id, nome, email, _ = valores
        
        # Limpa os campos antes de preencher
        self._limpar_campos_cadastro_e_gerenciamento('gerenciamento') 

        entries = [(self.id_entry, cliente_id), 
                   (self.nome_update_entry, nome), 
                   (self.email_update_entry, email)]
        
        for entry, value in entries:
            entry.insert(0, value)
        
        messagebox.showinfo("Ação", f"Dados do Cliente ID {cliente_id} carregados para Gerenciamento.")

    # --- Métodos de Manipulação de Dados (Handles) ---

    def _handle_cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()

        if not nome or not email:
            messagebox.showerror("Erro", "Nome e Email são obrigatórios!")
            return

        if self.cliente_dao.inserir_cliente(nome, email, telefone):
            messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
            # ⬅️ NOVO: Limpa os campos de Cadastro após sucesso
            self._limpar_campos_cadastro_e_gerenciamento('cadastro')
            self._carregar_dados_clientes() 
        else:
            messagebox.showerror("Erro de DB", "Falha ao cadastrar cliente.")

    def _handle_atualizar(self):
        try:
            cliente_id = int(self.id_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "ID do Cliente deve ser um número inteiro.")
            return

        novo_nome = self.nome_update_entry.get()
        novo_email = self.email_update_entry.get()
        
        if not novo_nome and not novo_email:
            messagebox.showerror("Erro", "Preencha ao menos o Novo Nome ou o Novo Email para atualizar.")
            return

        linhas_afetadas = self.cliente_dao.atualizar_cliente(cliente_id, novo_nome, novo_email)
        
        if linhas_afetadas == 1:
            messagebox.showinfo("Sucesso", f"Cliente ID {cliente_id} atualizado com sucesso!")
            # ⬅️ NOVO: Limpa os campos de Gerenciamento após sucesso
            self._limpar_campos_cadastro_e_gerenciamento('gerenciamento')
            self._carregar_dados_clientes() 
        elif linhas_afetadas == 0:
            messagebox.showwarning("Aviso", f"Cliente ID {cliente_id} não encontrado.")
        elif linhas_afetadas == -1:
            messagebox.showerror("Erro de DB", "Falha ao atualizar cliente.")


    def _handle_deletar(self):
        try:
            cliente_id = int(self.id_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "ID do Cliente deve ser um número inteiro.")
            return
            
        if not messagebox.askyesno("Confirmação", f"Tem certeza que deseja deletar o Cliente ID {cliente_id}?"):
            return

        linhas_afetadas = self.cliente_dao.deletar_cliente(cliente_id)

        if linhas_afetadas == 1:
            messagebox.showinfo("Sucesso", f"Cliente ID {cliente_id} deletado com sucesso.")
            # ⬅️ NOVO: Limpa os campos de Gerenciamento após deletar
            self._limpar_campos_cadastro_e_gerenciamento('gerenciamento')
            self._carregar_dados_clientes()
        elif linhas_afetadas == 0:
            messagebox.showwarning("Aviso", f"Cliente ID {cliente_id} não encontrado.")
        elif linhas_afetadas == -1:
            messagebox.showerror("Erro de DB", "Falha ao deletar cliente.")
            
    def run(self):
        self.master.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.master.mainloop()

    def _on_closing(self):
        self.cliente_dao.db_manager.fechar()
        self.master.destroy()

# =================================================================
# 4. Bloco de Execução Principal (Ponto de Entrada)
# =================================================================

if __name__ == "__main__":
    
    # ⚠️ 1. CONFIGURE SUAS CREDENCIAIS REAIS AQUI!
    db_config = {
        "dbname": "empresa", 
        "user": "postgres", 
        "password": "123456", 
        "host": "localhost",
        "port": "5432" 
    }
    
    # 2. Inicializa o gerenciador de banco de dados
    try:
        # Note: A classe Conexao deve ser importada de 'Classes.Conexao'
        db_manager = Conexao(**db_config) 
    except Exception as e:
        print(f"ERRO CRÍTICO: Falha ao instanciar a Conexao. {e}")
        exit()

    # 3. Conecta e inicia a aplicação
    if db_manager.conectar():
        # Note: A classe ClienteDao deve ser importada de 'Classes.ClienteDao'
        cliente_dao = ClienteDao(db_manager) 
        
        root = tk.Tk()
        root.resizable(False, False)
        
        app = Tela(root, cliente_dao)
        app.run()
    else:
        print("Aplicação encerrada devido à falha na conexão com o banco de dados.")