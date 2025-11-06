# Conteúdo INCORRETO em Classes/Cliente.py
class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf  = cpf    # Isto apenas tenta ACESSAR (o que falha pois ele não existe)
        self.nome = nome     # Isto apenas tenta ACESSAR
        self.endereco = endereco  # Isto apenas tenta ACESSAR