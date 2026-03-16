import customtkinter as ctk
import ollama
import json
import psycopg2
from psycopg2.extras import Json
import re

# Configuração visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Rastreamento Metamórfico IA")
        self.geometry("900x700")

        # Layout
        self.grid_columnconfigure(0, weight=1)
        
        # Título
        self.label = ctk.CTkLabel(self, text="Parser de Protocolos com Llama 3.1", font=("Roboto", 24, "bold"))
        self.label.pack(pady=20)

        # Entrada da String
        self.entry_label = ctk.CTkLabel(self, text="Cole a String HEX/ASCII do Rastreador:")
        self.entry_label.pack()
        self.entry = ctk.CTkEntry(self, width=700, placeholder_text="Ex: 78781F120B081D112E1FCC0271D0A20668CB0001750D0A")
        self.entry.pack(pady=10)

        # Botão de Processar
        self.btn_processar = ctk.CTkButton(self, text="Interpretar e Salvar no Banco", command=self.processar_dados)
        self.btn_processar.pack(pady=20)

        # Área de Resultado (IA)
        self.res_label = ctk.CTkLabel(self, text="Anatomia do Protocolo (Entendimento da IA):")
        self.res_label.pack()
        self.text_area = ctk.CTkTextbox(self, width=700, height=300)
        self.text_area.pack(pady=10)

        # Status do Banco
        self.status_label = ctk.CTkLabel(self, text="Status: Aguardando...", text_color="gray")
        self.status_label.pack(pady=10)

    def processar_dados(self):
        string_bruta = self.entry.get()
        if not string_bruta:
            self.status_label.configure(text="Erro: Cole uma string válida!", text_color="red")
            return

        self.status_label.configure(text="IA processando... aguarde.", text_color="yellow")
        self.update()

        # 1. Chamada para o Ollama
        try:
            prompt_sistema = """
            Você é um engenheiro de protocolos. Analise a string e retorne APENAS um JSON:
            {
                "plataforma": {"id": "string", "lat": float, "lng": float, "vel": float, "ign": bool, "status": "string"},
                "anatomia": {"fatiamento": "explicação"}
            }
            """
            
            response = ollama.chat(model='llama3.1', messages=[
                {'role': 'system', 'content': prompt_sistema},
                {'role': 'user', 'content': f"Analise: {string_bruta}"}
            ])

            conteudo = response['message']['content']
            json_match = re.search(r'\{.*\}', conteudo, re.DOTALL)
            
            if json_match:
                dados = json.loads(json_match.group())
                
                # Exibe na tela a anatomia
                self.text_area.delete("0.0", "end")
                self.text_area.insert("0.0", json.dumps(dados['anatomia'], indent=4, ensure_ascii=False))

                # 2. Salva no PostgreSQL
                self.salvar_db(string_bruta, dados)
            
        except Exception as e:
            self.text_area.insert("0.0", f"Erro: {str(e)}")
            self.status_label.configure(text="Erro no processamento.", text_color="red")

    def salvar_db(self, raw_hex, analise):
        try:
            conn = psycopg2.connect(dbname="seu_banco", user="postgres", password="123", host="localhost")
            cur = conn.cursor()
            
            p = analise['plataforma']
            sql = """
            INSERT INTO tb_telemetria_ia 
            (dispositivo_id, protocolo_nome, latitude, longitude, velocidade, ignicao, alerta_status, anatomia_string, payload_bruto)
            VALUES (%s, 'Identificado pela IA', %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (p['id'], p['lat'], p['lng'], p['vel'], p['ign'], p['status'], Json(analise['anatomia']), raw_hex))
            
            conn.commit()
            cur.close()
            conn.close()
            self.status_label.configure(text="Sucesso! Dados inseridos no PostgreSQL.", text_color="green")
        except Exception as e:
            self.status_label.configure(text=f"Erro Banco: {e}", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()