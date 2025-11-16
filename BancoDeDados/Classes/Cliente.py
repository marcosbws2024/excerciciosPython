from datetime import date # Importamos 'date' para lidar com a data de cadastro

class Pessoa:
    # A classe Pessoa permanece a mesma da resposta anterior, 
    # mantendo os atributos: __nome, __endereco, __telefone, __email
    def __init__(self, nome, endereco, telefone, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
    
    # ... (Todos os Getters e Setters de Pessoa estariam aqui) ...

    def get_nome(self):
        return self.__nome
    
    # Adicionando um __str__ básico para Pessoa (apenas para referência)
    def __str__(self):
        return f"Nome: {self.get_nome()}, Email: {self.__email}"


class Cliente(Pessoa):
    def __init__(self, nome, endereco, telefone, email, id_cliente, cpf, data_cadastro, status, tipo_cliente):
        # 1. Chamada ao construtor da classe pai (Pessoa)
        super().__init__(nome, endereco, telefone, email)
        
        # 2. Atributos Privados Específicos de Cliente
        self.__id_cliente = id_cliente
        self.__cpf = cpf
        self.__data_cadastro = data_cadastro # Espera um objeto date
        self.__status = status               # Ex: 'Ativo', 'Inativo'
        self.__tipo_cliente = tipo_cliente   # Ex: 'VIP', 'Padrão'

    # --- 🔎 Getters Específicos de Cliente ---

    def get_id_cliente(self):
        """Retorna o ID único do cliente."""
        return self.__id_cliente

    def get_cpf(self):
        """Retorna o CPF do cliente."""
        return self.__cpf

    def get_data_cadastro(self):
        """Retorna a data em que o cliente foi cadastrado."""
        return self.__data_cadastro

    def get_status(self):
        """Retorna o status atual do cliente (Ex: Ativo)."""
        return self.__status

    def get_tipo_cliente(self):
        """Retorna o tipo de cliente (Ex: VIP)."""
        return self.__tipo_cliente

    # --- ✏️ Setters Específicos de Cliente ---
    
    def set_id_cliente(self, novo_id):
        """Define um novo ID para o cliente (geralmente não é alterado)."""
        self.__id_cliente = novo_id

    def set_cpf(self, novo_cpf):
        """Define um novo CPF (com validação simples de comprimento)."""
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self.__cpf = novo_cpf
        else:
            print("Erro: CPF deve ter 11 dígitos numéricos.")

    def set_data_cadastro(self, nova_data):
        """Define a data de cadastro (espera um objeto date)."""
        if isinstance(nova_data, date):
            self.__data_cadastro = nova_data
        else:
            print("Erro: A data de cadastro deve ser um objeto 'date'.")

    def set_status(self, novo_status):
        """Altera o status do cliente."""
        if novo_status in ['Ativo', 'Inativo', 'Suspenso']:
            self.__status = novo_status
        else:
            print("Erro: Status inválido.")

    def set_tipo_cliente(self, novo_tipo):
        """Altera o tipo/categoria do cliente."""
        self.__tipo_cliente = novo_tipo

    # --- Representação Amigável ---
    def __str__(self):
        info_pessoa = super().__str__()
        return (f"CLIENTE ({info_pessoa})\n"
                f"  ID: {self.__id_cliente} | CPF: {self.__cpf}\n"
                f"  Status: {self.__status} | Tipo: {self.__tipo_cliente}\n"
                f"  Cadastro: {self.__data_cadastro.strftime('%d/%m/%Y')}") # Formata a data