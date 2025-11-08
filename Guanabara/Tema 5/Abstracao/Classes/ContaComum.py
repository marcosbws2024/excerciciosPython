from Classes.ContaCliente import ContaCliente

class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)
        
    def calculoRendimento(self):
        remuneracao = self.valorInvestido * self.taxaRendimento
        valorIOF = remuneracao * self.IOF
        self.valorInvestido += remuneracao - valorIOF