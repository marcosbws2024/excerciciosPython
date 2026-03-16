import customtkinter as ctk
from tkinter import filedialog
import ollama
import json
import psycopg2
from psycopg2.extras import Json

class TelaAprendizado(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Módulo de Aprendizado de Protocolos - TrackIA")
        self.geometry("600x500")

        self.label = ctk.CTkLabel(self, text="Treinar IA com Manual Técnico", font=("Roboto", 20))
        self.label.pack(pady=20)

        self.btn_file = ctk.CTkButton(self, text="Selecionar Manual (PDF/TXT/CSV)", command=self.upload_file)
        self.btn_file.pack(pady=10)

        self.nome_proto = ctk.CTkEntry(self, placeholder_text="Nome do Protocolo (ex: Suntech_v2)")
        self.nome_proto.pack(pady=10)

        self.status_box = ctk.CTkTextbox(self, width=500, height=200)
        self.status_box.pack(pady=10)

        self.btn_treinar = ctk.CTkButton(self, text="Ensinar ao Llama 3.1", fg_color="green", command=self.treinar_ia)
        self.btn_treinar.pack(pady=20)

    def upload_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path = path
            self.status_box.insert("end", f"Arquivo carregado: {path}\n")

    def treinar_ia(self):
        # Aqui a IA lê o conteúdo do arquivo e gera um mapa de fatiamento
        # Simulando a extração de conhecimento:
        self.status_box.insert("end", "IA lendo manual e extraindo offsets... aguarde.\n")
        self.update()

        conteudo_manual = "Simulação do conteúdo lido do arquivo..." 
        
        prompt = f"""
        Analise este manual técnico: {conteudo_manual}
        Crie um MAPA DE FATIAMENTO para o protocolo {self.nome_proto.get()}.
        Retorne APENAS um JSON com os offsets de cada campo (ex: 'latitude': [20, 28]).
        """

        try:
            response = ollama.chat(model='llama3.1', messages=[{'role': 'user', 'content': prompt}])
            regras = response['message']['content']
            
            # Salva na base de conhecimento
            self.salvar_conhecimento(self.nome_proto.get(), regras)
            self.status_box.insert("end", "Protocolo aprendido e salvo no Cérebro do Sistema!\n")
        except Exception as e:
            self.status_box.insert("end", f"Erro: {e}\n")

    def salvar_conhecimento(self, nome, regras):
        conn = psycopg2.connect(dbname="seu_banco", user="postgres", password="123", host="localhost")
        cur = conn.cursor()
        cur.execute("INSERT INTO base_conhecimento_protocolos (nome_protocolo, regras_fatiamento) VALUES (%s, %s)", (nome, regras))
        conn.commit()
        cur.close()
        conn.close()

if __name__ == "__main__":
    app = TelaAprendizado()
    app.mainloop()