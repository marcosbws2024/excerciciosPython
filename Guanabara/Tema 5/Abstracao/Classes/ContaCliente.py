from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self,numero,IOF,IR,valorInvestido,taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento
    
    @abstractmethod
    def calculoRendimento(self):
        remuneracao = self.valorInvestido * self.taxaRendimento
        valorIOF = remuneracao * self.IOF
        valorIR = remuneracao * self.IR
        self.valorInvestido += remuneracao - valorIOF - valorIR
        
    def extrato(self):
        print(f"O Saldo atual da Conta {self.numero} é {self.valorInvestido:10.2f}")