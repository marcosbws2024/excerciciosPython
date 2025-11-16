class Pessoa:
    def __init__(self, nome, endereco, telefone, email):
        # Variáveis privadas (Encapsuladas)
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

    # --- 🔎 Getters (Métodos para Obter os Valores) ---

    def get_nome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    def get_endereco(self):
        """Retorna o endereço da pessoa."""
        return self.__endereco

    def get_telefone(self):
        """Retorna o telefone da pessoa."""
        return self.__telefone

    def get_email(self):
        """Retorna o e-mail da pessoa."""
        return self.__email

    # --- ✏️ Setters (Métodos para Modificar os Valores) ---

    def set_nome(self, novo_nome):
        """Define um novo nome."""
        # Poderia haver validação aqui
        self.__nome = novo_nome

    def set_endereco(self, novo_endereco):
        """Define um novo endereço."""
        self.__endereco = novo_endereco

    def set_telefone(self, novo_telefone):
        """Define um novo telefone com validação simples."""
        if isinstance(novo_telefone, str) and len(novo_telefone) >= 8:
            self.__telefone = novo_telefone
        else:
            print("Erro: Telefone inválido. Deve ser uma string com pelo menos 8 dígitos.")

    def set_email(self, novo_email):
        """Define um novo e-mail com validação simples."""
        if "@" in novo_email and "." in novo_email:
            self.__email = novo_email
        else:
            print("Erro: E-mail inválido. Deve conter '@' e '.'.")

    # Método para facilitar a visualização do objeto
    def __str__(self):
        return (f"Pessoa(Nome: {self.__nome}, Telefone: {self.__telefone}, "
                f"Email: {self.__email}, Endereço: {self.__endereco})")