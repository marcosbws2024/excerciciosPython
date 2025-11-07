class Extrato:
    
    def __init__(self):
        self.transacoes = []
    
    def gerarExtrato(self,conta):
        print(f"Extrato da Conta: {conta}")
        for t in self.transacoes:
            print(f"{t[0]:15s} {t[1]:10.2f} {t[2].strftime('%d/%b/%Y')}")    
    # 0 - Tipo
    # 1 - Valor
    # 2 - Data
    