import tkinter as tk
from tkinter import ttk
import pandas as pd

# Inicialização da Janela
janela = tk.Tk()
janela.title("Sistema de Cadastro de Alunos")
janela.geometry("820x600")

# --- CRIAÇÃO E EXIBIÇÃO DOS COMPONENTES ---

lblNome = tk.Label(janela, text="Nome do Aluno:")
lblNome.pack() # Faltava o pack
txtNome = tk.Entry(janela, bd=3)
txtNome.pack(pady=5)

lblNota1 = tk.Label(janela, text="Nota 1:")
lblNota1.pack() # Faltava o pack
txtNota1 = tk.Entry(janela)
txtNota1.pack(pady=5)

lblNota2 = tk.Label(janela, text="Nota 2:")
lblNota2.pack() # Faltava o pack
txtNota2 = tk.Entry(janela)
txtNota2.pack(pady=5)

# --- CONFIGURAÇÃO DA TABELA ---
colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    treeMedias.heading(coluna, text=coluna)
    treeMedias.column(coluna, width=120, anchor="center")

treeMedias.pack(padx=10, pady=10)

# Scrollbar
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
treeMedias.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# --- FUNÇÕES ---

def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Em Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao

def salvar_dados():
    dados = []
    for line in treeMedias.get_children():
        valores = treeMedias.item(line)["values"]
        dados.append(valores)

    if dados: # Só salva se houver dados
        df = pd.DataFrame(data=dados, columns=colunas)
        df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")
        print("Dados salvos em planilhaAlunos.xlsx")

def cadastrar_aluno():
    try:
        nome = txtNome.get()
        n1 = float(txtNota1.get())
        n2 = float(txtNota2.get())

        if not nome:
            print("Erro: O nome é obrigatório.")
            return

        media, situacao = verificar_situacao(n1, n2)
        treeMedias.insert("", "end", values=(nome, n1, n2, f"{media:.2f}", situacao))
        salvar_dados()
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos (use ponto para decimais).")
    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")

def carregar_dados_iniciais():
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")
        for _, row in df.iterrows():
            treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
        print("Dados carregados da planilha.")
    except FileNotFoundError:
        print("Nenhum arquivo de planilha encontrado. Começando do zero.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

# Botão de cadastro
btnCadastrar = tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno, bg="#4CAF50", fg="white")
btnCadastrar.pack(pady=10)

# Carregar dados ao iniciar e abrir a janela
carregar_dados_iniciais()
janela.mainloop()