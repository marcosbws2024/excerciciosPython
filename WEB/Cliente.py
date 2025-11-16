from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, email, id=None):
        super().__init__(nome, email)
        self.id = id # O ID será gerado pelo banco de dados
    
    def to_dict(self):
        """Retorna o objeto como um dicionário para serialização JSON."""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }