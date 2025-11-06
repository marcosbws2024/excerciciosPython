class Extrato:
    
    def __init__(self):
        self.transacoes = []
    
    def gerarExtrato(self,conta):
        print(f"Extrato da Conta: {conta}")
        for transacao in self.transacoes:
            print(f"{transacao[0]:15s} {transacao[1]:10.2f} {transacao[2].strftime('%d/%b/%Y')}")    
    # 0 - Tipo
    # 1 - Valor
    # 2 - Data
    