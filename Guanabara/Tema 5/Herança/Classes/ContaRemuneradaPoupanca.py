from Classes.Conta import Conta
from Classes.Poupanca import Poupanca

class ContaRemuneradaPoupance(Conta,Poupanca):
    def __init__(self, clientes, numero, saldo,taxaRemuneracao):
        Conta.__init__(self,clientes,numero,saldo)
        Poupanca.__init__(self,taxaRemuneracao)
        
        def remuneraConta(self):
            self.saldo +=self.saldo * (self.taxaRemuneracao / 30)