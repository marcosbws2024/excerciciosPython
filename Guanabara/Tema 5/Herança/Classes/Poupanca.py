
class Poupanca:
    
    def __init__(self,taxaRemuneracao):
        self.taxaRemuneracao = taxaRemuneracao
    
    def remuneraConta(self):
        self.saldo+= self.saldo * self.taxaRemeneracao
        
    