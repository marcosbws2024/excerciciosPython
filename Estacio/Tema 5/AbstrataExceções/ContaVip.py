from ContaCliente import ContaCliente

class ContaVip(ContaCliente):
    def calculo_rendimento(self):
        # Implementação fictícia para cálculo de rendimento
        return self.valor_investido * self.taxa_rendimento - (self.IOF + self.IR)

# Instanciando a subclasse concreta
cc1 = ContaVip(1, 0.1, 0.25, 1000, 0.8)
