# conexao.py

import psycopg2
from Cliente import Cliente

# ⚠️ Configure suas credenciais aqui
class DBConfig:
    DBNAME = "empresa"
    USER = "postgres"
    PASSWORD = "123456"
    HOST = "localhost"
    PORT = "5432"

class Conexao:
    """Gerencia a conexão com o PostgreSQL."""
    @staticmethod
    def get_conn():
        return psycopg2.connect(
            dbname=DBConfig.DBNAME,
            user=DBConfig.USER,
            password=DBConfig.PASSWORD,
            host=DBConfig.HOST,
            port=DBConfig.PORT
        )

