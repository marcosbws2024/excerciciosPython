import customtkinter as ctk
from tkinter import filedialog, messagebox
import ollama
import json
import psycopg2
from psycopg2.extras import Json
from PyPDF2 import PdfReader
import re

ctk.set_appearance_mode("dark")

class PlataformaTrackIA(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TrackIA - Parser Metamórfico Universal")
        self.geometry("1000x800")

        # --- Layout de Abas ---
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        self.tabview.add("Decodificador")
        self.tabview.add("Treinar IA (Upload Manual)")

        self.setup_aba_decodificador()
        self.setup_aba_treinamento()

    def setup_aba_decodificador(self):
        # Aba 1: Decodificação de Strings
        parent = self.tabview.tab("Decodificador")
        
        ctk.CTkLabel(parent, text="Cole a String do Rastreador:", font=("Roboto", 16)).pack(pady=10)
        self.entry_hex = ctk.CTkEntry(parent, width=800, placeholder_text="Ex: 78781F12...")
        self.entry_hex.pack(pady=5)

        self.btn_decodificar = ctk.CTkButton(parent, text="Decodificar com IA Local", command=self.fluxo_decodificacao)
        self.btn_decodificar.pack(pady=20)

        self.txt_resultado = ctk.CTkTextbox(parent, width=800, height=400)
        self.txt_resultado.pack(pady=10)

    def setup_aba_treinamento(self):
        # Aba 2: Treinamento por PDF
        parent = self.tabview.tab("Treinar IA (Upload Manual)")
        
        ctk.CTkLabel(parent, text="Ensine um Novo Protocolo à IA", font=("Roboto", 18, "bold")).pack(pady=20)
        
        self.btn_upload = ctk.CTkButton(parent, text="Selecionar Manual PDF", fg_color="transparent", border_width=2, command=self.upload_pdf)
        self.btn_upload.pack(pady=10)
        
        self.label_path = ctk.CTkLabel(parent, text="Nenhum arquivo selecionado", text_color="gray")
        self.label_path.pack()

        self.entry_proto_name = ctk.CTkEntry(parent, width=300, placeholder_text="Nome do Protocolo (ex: ST300_V2)")
        self.entry_proto_name.pack(pady=20)

        self.btn_treinar = ctk.CTkButton(parent, text="Processar Manual e Aprender", fg_color="green", command=self.fluxo_treinamento)
        self.btn_treinar.pack(pady=10)

    # --- LÓGICA DE PDF ---
    def upload_pdf(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            self.file_path = path
            self.label_path.configure(text=f"Selecionado: {path.split('/')[-1]}", text_color="white")

    def ler_pdf(self, caminho):
        texto = ""
        try:
            reader = PdfReader(caminho)
            # Lemos as primeiras 5 páginas para não estourar a memória da IA
            for i in range(min(5, len(reader.pages))):
                texto += reader.pages[i].extract_text()
            return texto
        except Exception as e:
            return str(e)

    # --- LÓGICA DE IA E BANCO ---
    def fluxo_treinamento(self):
        nome = self.entry_proto_name.get()
        if not hasattr(self, 'file_path') or not nome:
            messagebox.showerror("Erro", "Selecione um PDF e dê um nome ao protocolo.")
            return

        texto_manual = self.ler_pdf(self.file_path)
        
        prompt = f"Analise este manual técnico e extraia as regras de fatiamento (offsets) para o protocolo {nome}. Retorne apenas JSON."
        
        try:
            response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': f"{prompt}\n\nTexto: {texto_manual}"}])
            regras = response['message']['content']
            
            # Salva na base de conhecimento (PostgreSQL)
            self.salvar_no_banco_conhecimento(nome, regras)
            messagebox.showinfo("Sucesso", f"A IA aprendeu o protocolo {nome}!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no treinamento: {e}")

    def salvar_no_banco_conhecimento(self, nome, regras):
        # Conexão PostgreSQL (ajuste seus dados aqui)
        conn = psycopg2.connect(dbname="seu_banco", user="postgres", password="123", host="localhost")
        cur = conn.cursor()
        cur.execute("INSERT INTO base_conhecimento_protocolos (nome_protocolo, regras_fatiamento) VALUES (%s, %s) ON CONFLICT (nome_protocolo) DO UPDATE SET regras_fatiamento = EXCLUDED.regras_fatiamento", (nome, regras))
        conn.commit()
        cur.close()
        conn.close()

    def fluxo_decodificacao(self):
        string_hex = self.entry_hex.get()
        # Aqui a IA busca no banco o que aprendeu e aplica na string
        # (Lógica simplificada para o exemplo)
        response = ollama.chat(model='llama3.1', messages=[
            {'role': 'system', 'content': "Você é um parser que usa sua base de conhecimento para decodificar telemetria."},
            {'role': 'user', 'content': f"Decodifique esta string: {string_hex}"}
        ])
        
        self.txt_resultado.delete("0.0", "end")
        self.txt_resultado.insert("0.0", response['message']['content'])

if __name__ == "__main__":
    app = PlataformaTrackIA()
    app.mainloop()