import sqlite3
import os


def conectar_banco(nome_banco):
    # Encontra o caminho da pasta onde o script está
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(diretorio_atual, nome_banco)

    conexao = sqlite3.connect(caminho_completo)
    # Importante: Ativa o suporte a chaves estrangeiras no SQLite
    conexao.execute("PRAGMA foreign_keys = ON;")
    return conexao


def criar_tabelas(conexao):
    cursor = conexao.cursor()

    # Tabela de Locais
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Locais (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      endereco TEXT NOT NULL)"""
    )

    # Tabela de Eventos (depende de Locais)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Eventos (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      data TEXT NOT NULL,
                      local_id INTEGER NOT NULL,
                      FOREIGN KEY(local_id) REFERENCES Locais(id))"""
    )

    # Tabela de Participantes (depende de Eventos)
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Participantes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT NOT NULL,
                      email TEXT NOT NULL,
                      evento_id INTEGER NOT NULL,
                      FOREIGN KEY(evento_id) REFERENCES Eventos(id))"""
    )

    conexao.commit()
    print("Banco de dados e tabelas configurados com sucesso!")


# O bloco principal deve ficar fora das funções (coluna 0)
if __name__ == "__main__":
    minha_conexao = conectar_banco("eventos.db")
    criar_tabelas(minha_conexao)
    minha_conexao.close()
