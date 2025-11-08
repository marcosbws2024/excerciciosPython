class Banco:
    def __init__(self,codigo,nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []
        
    def adicionaConta(self,contaCliente):
        self.contas.append(contaCliente)
        
    def calcularRendimentoMensal(self):
        for c in self.contas:
            c.calculoRendimento()
    
    def imprimeSaldoContas(self):
        for c in self.contas:
            c.extrato()