class Conta:

    #metodo construtor.
    def __init__(self, numero, cpf, nomeTitular, saldo):
        #self está apontando para si mesmo na classe assim como o this no java
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo+=valor
    
    def sacar(self,valor):
        if self.saldo <valor:
            return False
        else: 
            self.saldo -= valor
            return True
    
    def gerar_extrato(self):
         print(f'Numero:{self.numero}\nCPF:{self.cpf}\nSaldo:{self.saldo}')
    
    def transferenciaValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Não existe Saldo o Suficiente")
        else:
             contaDestino.depositar(valor)
             self.saldo -= valor
             return ("Tranferencia realizada")
    
    
    
# instanciando a classe e executando o teste
def main():
    c1 = Conta(1, 1, "João", 1000)
    c2 = Conta(3,456,'Maria',0)
    
    if c1 != c2:
        print("Endereços de memoria diferentes")
    
    print(c1)
    print(c2)
    print(c1.saldo)
    print(c2.saldo)
    c1.depositar(300)
    c2.depositar(400)
   
    print('Deposito realizado: ')
    c1.depositar(300)
    print("Extrato:")
    c1.gerar_extrato()
    
    valor_saque = 150
    resultado_saque = c1.sacar(valor_saque)
    if resultado_saque:
        print(f'Saque de R${valor_saque} realizado com sucesso!')
        print(f'Saldo Atual:R$:{c1.saldo}')
    else:
        print("Saldo Insuficiente para realizar o Saque!!!")
 
 
 
    c1.transferenciaValor(c2,500)
    print("Transferencia realizada")
     
    print("Extrato Conta 1:")
    c1.gerar_extrato()
    print("Extrato Conta 2:")
    c2.gerar_extrato()
    


if __name__ == "__main__":
    main()