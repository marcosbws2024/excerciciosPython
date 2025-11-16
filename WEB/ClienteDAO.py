from Cliente import Cliente
from Conexao import Conexao
import psycopg2

class ClienteDAO:
    """DAO para operações CRUD em Clientes."""
    
    def __init__(self):
        self._setup_db()

    def _setup_db(self):
        """Cria a tabela 'tabela_web' se não existir, com ID, Nome e Email."""
        conn = None
        try:
            conn = Conexao.get_conn()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tabela_web (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                );
            """)
            conn.commit()
            cursor.close()
            print("✅ Tabela 'tabela_web' verificada/criada no banco de dados.")
        except psycopg2.Error as e:
            print(f"❌ Erro ao configurar DB: {e}")
        finally:
            if conn:
                conn.close()

    def inserir(self, cliente: Cliente):
        conn = None
        try:
            conn = Conexao.get_conn()
            cursor = conn.cursor()
            # Query atualizada para usar tabela_web
            cursor.execute(
                "INSERT INTO tabela_web (nome, email) VALUES (%s, %s) RETURNING id;",
                (cliente.nome, cliente.email)
            )
            cliente.id = cursor.fetchone()[0]
            conn.commit()
            return cliente
        except psycopg2.Error as e:
            print(f"Erro ao inserir: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def buscar_todos(self):
        conn = None
        clientes = []
        try:
            conn = Conexao.get_conn()
            cursor = conn.cursor()
            # Query atualizada para usar tabela_web
            cursor.execute("SELECT id, nome, email FROM tabela_web ORDER BY id;")
            
            for row in cursor.fetchall():
                clientes.append(Cliente(id=row[0], nome=row[1], email=row[2]).to_dict())
            
            return clientes
        except psycopg2.Error as e:
            print(f"Erro ao buscar: {e}")
            return []
        finally:
            if conn:
                conn.close()