# cliente_dao.py

# Importa a classe de conexão que está no arquivo conexao.py
from Classes.Conexao import Conexao 

class ClienteDao:
    """DAO: Encapsula as operações CRUD específicas para a entidade Cliente."""
    def __init__(self, conexao: Conexao):
        self.db_manager = conexao
        self._criar_tabela_se_nao_existe()

    def _criar_tabela_se_nao_existe(self):
        """Cria a tabela de clientes se não existir."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE,
            telefone VARCHAR(20)
        );
        """
        self.db_manager.executar_query(create_table_query, commit=True)
        # print("Tabela 'clientes' verificada/criada.")

    def inserir_cliente(self, nome, email, telefone):
        """Insere um novo cliente no banco de dados."""
        query = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s);"
        params = (nome, email, telefone)
        return self.db_manager.executar_query(query, params, commit=True)

    def atualizar_cliente(self, cliente_id, novo_nome, novo_email):
        """Atualiza o nome e/ou email de um cliente existente pelo ID."""
        query = "UPDATE clientes SET nome = %s, email = %s WHERE id = %s;"
        params = (novo_nome, novo_email, cliente_id)
        
        if self.db_manager.executar_query(query, params, commit=True):
            return self.db_manager.cursor.rowcount
        return -1

    def deletar_cliente(self, cliente_id):
        """Deleta um cliente pelo ID."""
        query = "DELETE FROM clientes WHERE id = %s;"
        params = (cliente_id,)

        if self.db_manager.executar_query(query, params, commit=True):
            return self.db_manager.cursor.rowcount
        return -1

    def buscar_todos_clientes(self):
        """Busca todos os clientes e retorna como uma lista de tuplas."""
        query = "SELECT id, nome, email, telefone FROM clientes ORDER BY id;"
        resultados = self.db_manager.executar_query(query)
        if resultados is not False:
            return resultados
        return []