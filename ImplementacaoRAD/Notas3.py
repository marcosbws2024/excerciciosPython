usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}



def abrir_tela_login():
    login_win = tk.Toplevel()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack()
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuarios[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario, usuario)
        else:
            tk.messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(login_win, text="Entrar", command=validar_login).pack()


janela = tk.Tk()
janela.withdraw()  # Oculta a janela principal
abrir_tela_login()
janela.mainloop()



def carregar_dados(usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")

        treeMedias.delete(*treeMedias.get_children())  # Limpa a tabela antes de atualizar

        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
        else:
            df_aluno = df[df["Aluno"] == usuario]  # Filtra os dados do aluno logado
            for _, row in df_aluno.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado.")

def iniciar_sistema(tipo_usuario, usuario):
    janela.deiconify()  # Exibe a janela principal
    carregar_dados(usuario, tipo_usuario)


def cadastrar_aluno():
    if tipo_usuario != "professor":
        tk.messagebox.showwarning("Acesso Negado", "Somente professores podem adicionar alunos.")
        return
    
    try:
        nome = txtNome.get()
        nota1 = float(txtNota1.get())
        nota2 = float(txtNota2.get())

        media, situacao = verificar_situacao(nota1, nota2)

        treeMedias.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
        salvar_dados()
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")

def excluir_aluno():
    if tipo_usuario != "professor":
        tk.messagebox.showwarning("Acesso Negado", "Somente professores podem excluir registros.")
        return

    
    selected_item = treeMedias.selection()
    if not selected_item:
        tk.messagebox.showerror("Erro", "Nenhum aluno selecionado para exclusão.")
        return

    treeMedias.delete(selected_item)
salvar_dados()


btnExcluir = tk.Button(janela, text="Excluir Aluno", command=excluir_aluno)
if tipo_usuario == "professor":
    btnExcluir.pack()
