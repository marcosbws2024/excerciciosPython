from Classes.Conta import Conta
from Poupanca import Poupanca

class ContaRemuneradaPoupance(Conta,Poupanca):
    def __init__(self, clientes, numero, saldo,taxaRemuneracao):
        Conta.__init__(clientes,numero,saldo)
        Poupanca.__init__(taxaRemuneracao)