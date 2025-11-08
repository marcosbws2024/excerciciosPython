from Classes.ContaCliente import ContaCliente

class ContaVip(ContaCliente):
     def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
          super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)
          
     def calculoRendimento(self):
          self.valorInvestido += self.valorInvestido * self.taxaRendimento