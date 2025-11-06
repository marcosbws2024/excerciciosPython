class Conta:
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.numero = numero 
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    
    def depositar(self,valor):
        self.saldo = self.saldo+valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else: 
            self.saldo = self.saldo-valor
            return True
        
    def gerarExtrato(self):
        print("="*20,"EXTRATO BANCARIO","="*20)
        print(f"Nome do Titular: {self.nomeTitular}")
        print(f"CPF: {self.cpf}")
        print(f"Numero da Conta: {self.numero}")
        print(f"Saldo: {self.saldo}")
        print("="*58)
    
    def tranfereValor(self,contaDestino,valor):
        if self.saldo <valor:
            return("Saldo Insuficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo =self.saldo - valor
            return("Tranferencia Realizada com Sucesso!!!")
        
  
conta1 = Conta(1,13156,"Marcos",1500)
conta1.depositar(500)
valorSaque = 150
resultadoSaque = conta1.sacar(valorSaque)

if resultadoSaque:
    print(f"O saque de Valor: R${valorSaque} foi realizado com sucesso")
else:
    print("Saldo Insuficiente!!!")
    
conta1.gerarExtrato()

conta2 = Conta(123,54687,"Maria",3500)

if(conta1==conta2):
    print("São iguais")
else:
    print("São diferentes")

print(conta1.tranfereValor(conta2,300))

conta2.gerarExtrato()
conta1.gerarExtrato()


        