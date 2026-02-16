import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

# --- CONFIGURAÇÃO DE UTILIZADORES ---
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}

# Variáveis globais para controlo de sessão
tipo_sessao = ""
usuario_logado = ""

def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7.0 else "Em Recuperação" if media >= 5.0 else "Reprovado"
    return media, situacao

def salvar_dados():
    colunas = ["Aluno", "Nota1", "Nota2", "Média", "Situação"]
    dados = []
    for line in treeMedias.get_children():
        valores = treeMedias.item(line)["values"]
        dados.append(valores)
    
    df = pd.DataFrame(data=dados, columns=colunas)
    df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")

def carregar_dados(usuario, tipo_usuario):
    try:
        if not os.path.exists("planilhaAlunos.xlsx"):
            return
        
        df = pd.read_excel("planilhaAlunos.xlsx")
        treeMedias.delete(*treeMedias.get_children())

        if tipo_usuario == "professor":
            df_mostrar = df
        else:
            # Importante: Garante que o aluno vê apenas a sua linha
            df_mostrar = df[df["Aluno"].astype(str).str.lower() == usuario.lower()]

        for _, row in df_mostrar.iterrows():
            treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except Exception as e:
        print(f"Erro ao carregar: {e}")

def cadastrar_aluno():
    if tipo_sessao != "professor":
        messagebox.showwarning("Acesso Negado", "Apenas professores podem adicionar dados.")
        return
    try:
        nome = txtNome.get()
        n1 = float(txtNota1.get())
        n2 = float(txtNota2.get())
        media, situacao = verificar_situacao(n1, n2)
        treeMedias.insert("", "end", values=(nome, n1, n2, f"{media:.2f}", situacao))
        salvar_dados()
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro", "Insira notas válidas.")

def excluir_aluno():
    if tipo_sessao != "professor":
        return
    selected = treeMedias.selection()
    if not selected:
        messagebox.showwarning("Aviso", "Selecione um aluno na tabela.")
        return
    treeMedias.delete(selected)
    salvar_dados()

def limpar_campos():
    txtNome.delete(0, "end")
    txtNota1.delete(0, "end")
    txtNota2.delete(0, "end")

# --- SISTEMA DE LOGIN ---
def abrir_tela_login():
    login_win = tk.Toplevel()
    login_win.title("Login do Sistema")
    login_win.geometry("300x200")
    login_win.grab_set() # Foca apenas nesta janela

    tk.Label(login_win, text="Utilizador:").pack(pady=5)
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        global tipo_sessao, usuario_logado
        user = entry_usuario.get()
        pw = entry_senha.get()

        if user in usuarios and usuarios[user]["senha"] == pw:
            tipo_sessao = usuarios[user]["tipo"]
            usuario_logado = user
            login_win.destroy()
            configurar_interface_por_tipo()
            janela.deiconify()
            carregar_dados(usuario_logado, tipo_sessao)
        else:
            messagebox.showerror("Erro", "Utilizador ou Senha incorretos!")

    tk.Button(login_win, text="Entrar", command=validar_login, bg="blue", fg="white").pack(pady=10)

def configurar_interface_por_tipo():
    # Se for aluno, esconde os controlos de edição
    if tipo_sessao == "aluno":
        frame_professor.pack_forget()
        btnExcluir.pack_forget()
    else:
        frame_professor.pack(pady=10, before=treeMedias)
        btnExcluir.pack(pady=5)

# --- INTERFACE PRINCIPAL ---
janela = tk.Tk()
janela.title("Sistema de Gestão Escolar")
janela.geometry("820x600")
janela.withdraw() # Esconde até o login ser feito

# Frame para inputs (Apenas Professor)
frame_professor = tk.Frame(janela)

tk.Label(frame_professor, text="Nome:").grid(row=0, column=0)
txtNome = tk.Entry(frame_professor)
txtNome.grid(row=0, column=1)

tk.Label(frame_professor, text="Nota 1:").grid(row=0, column=2)
txtNota1 = tk.Entry(frame_professor, width=5)
txtNota1.grid(row=0, column=3)

tk.Label(frame_professor, text="Nota 2:").grid(row=0, column=4)
txtNota2 = tk.Entry(frame_professor, width=5)
txtNota2.grid(row=0, column=5)

btnCadastrar = tk.Button(frame_professor, text="Cadastrar", command=cadastrar_aluno, bg="green", fg="white")
btnCadastrar.grid(row=0, column=6, padx=10)

# Tabela
colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    treeMedias.heading(col, text=col)
    treeMedias.column(col, width=120, anchor="center")
treeMedias.pack(pady=20)

btnExcluir = tk.Button(janela, text="Excluir Aluno Selecionado", command=excluir_aluno, bg="red", fg="white")

# Inicia o processo
abrir_tela_login()
janela.mainloop()