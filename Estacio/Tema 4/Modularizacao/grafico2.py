import tkinter as tk
from tkinter import messagebox
import psycopg2 # Necessário instalar: pip install psycopg2-binary

# --- DADOS DE CONEXÃO COM O BANCO DE DADOS ---
# ATENÇÃO: Substitua pelos seus próprios dados
DB_NAME = "seu_banco_de_dados"
DB_USER = "seu_usuario_postgres"
DB_PASS = "sua_senha_postgres"
DB_HOST = "localhost" # Geralmente é 'localhost' ou um IP
DB_PORT = "5432"      # Porta padrão do PostgreSQL

# --- SCRIPT SQL PARA CRIAÇÃO DE TABELA (DEIXADO NOS COMENTÁRIOS) ---
"""
-- 1. CRIE O BANCO DE DADOS (Execute no psql ou DBeaver/pgAdmin)
-- CREATE DATABASE seu_banco_de_dados;

-- 2. CRIE A TABELA DE USUÁRIOS
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
# -------------------------------------------------------------------

def conectar_bd():
    """Tenta estabelecer a conexão com o PostgreSQL e retorna o objeto de conexão e cursor."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        return conn, cursor
    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Não foi possível conectar ao banco de dados:\n{e}")
        return None, None

def cadastrar_usuario():
    """Função chamada ao clicar no botão para salvar o usuário no BD."""
    nome = entry_nome.get()
    email = entry_email.get()

    if not nome or not email:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    conn, cursor = conectar_bd()
    if conn is None:
        return

    try:
        # SQL para inserir dados
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s);"
        cursor.execute(sql, (nome, email))
        conn.commit() # Confirma a transação
        
        messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado com sucesso!")
        
        # Limpa os campos após o cadastro
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)

    except psycopg2.IntegrityError:
        messagebox.showerror("Erro de Cadastro", "Este e-mail já está cadastrado (violação da chave única).")
        conn.rollback() # Desfaz a transação em caso de erro

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o usuário: {e}")
        conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# --- CONFIGURAÇÃO DA INTERFACE TKINTER ---
root = tk.Tk()
root.title("Cadastro de Usuário - PostgreSQL")
root.geometry("350x200")
root.resizable(False, False)

# Labels e Campos de Entrada (Nome)
label_nome = tk.Label(root, text="Nome Completo:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# Labels e Campos de Entrada (Email)
label_email = tk.Label(root, text="E-mail:")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Botão de Cadastro
botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_usuario, width=15)
botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

# Inicia o loop principal da aplicação
root.mainloop()