import datetime
from Classes.Extrato import Extrato


class Conta:

    
    def __init__(self,clientes,numero,saldo):
        self.clientes = clientes 
        self.numero = numero
        self.saldo = saldo
        self.dataAbertura = datetime.datetime.today()
        self.extrato = Extrato()#Composição
     
 
        
    
    def depositar(self,valor):
        self.saldo = self.saldo+valor
        self.extrato.transacoes.append(["Deposito",valor,datetime.datetime.today()])
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else: 
            self.saldo = self.saldo-valor
            self.extrato.transacoes.append(["Saque",valor, datetime.datetime.today()])
            return True
        
    def gerarSaldo(self):
        print("="*20,"SALDO BANCARIO","="*20)
        #nomes_clientes = ", ".join([c.nome for c in self.clientes])
        #print(f"Titulares: {nomes_clientes}")
        print(f"Numero da Conta: {self.numero}")
        print(f"Saldo: {self.saldo}")
        print("="*58)
    
    def tranfereValor(self,contaDestino,valor):
        if self.saldo <valor:
            return("Saldo Insuficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo =self.saldo - valor
            self.extrato.transacoes.append(["Tranferencia",valor,datetime.datetime.today()])
            return("Tranferencia Realizada com Sucesso!!!")