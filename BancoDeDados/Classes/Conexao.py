# conexao.py

import psycopg2

class Conexao:
    """Gerencia a conexão base com o PostgreSQL e executa queries genéricas."""
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None

    def _criar_database_se_nao_existe(self):
        """Conecta temporariamente ao banco 'postgres' padrão para criar o banco alvo."""
        try:
            temp_conn = psycopg2.connect(
                dbname='postgres', 
                user=self.user, 
                password=self.password, 
                host=self.host, 
                port=self.port,
                client_encoding='utf8'
            )
            temp_conn.autocommit = True
            temp_cursor = temp_conn.cursor()

            temp_cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.dbname}'")
            if not temp_cursor.fetchone():
                temp_cursor.execute(f"CREATE DATABASE {self.dbname} ENCODING 'UTF8'")
                print(f"✅ Banco de dados '{self.dbname}' criado com sucesso.")
            
            temp_cursor.close()
            temp_conn.close()
            return True
        except psycopg2.Error as e:
            print(f"❌ Erro Crítico na pré-conexão: {e}")
            return False

    def conectar(self):
        """Estabelece a conexão principal."""
        if not self._criar_database_se_nao_existe():
            return False

        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                client_encoding='utf8' 
            )
            self.cursor = self.conn.cursor()
            print(f"✅ Conexão estabelecida com sucesso.")
            return True
        except psycopg2.Error as e:
            print(f"❌ Erro ao conectar com PostgreSQL: {e}") 
            return False

    def fechar(self):
        """Fecha a conexão com o banco de dados."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexão com PostgreSQL encerrada.")

    def executar_query(self, query, params=None, commit=False):
        """Executa uma consulta genérica (CRUD)."""
        if not self.conn:
            print("Erro: Nenhuma conexão ativa.")
            return False
            
        try:
            self.cursor.execute(query, params)
            if commit:
                self.conn.commit()
                return True
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            # print(f"Erro ao executar a query: {e}") # Descomentar para debug
            if self.conn:
                self.conn.rollback()
            return False