class Conta2:
    __totalContas  = 0
    
    @staticmethod
    def nomeBanco():
        return "Banco do Marcao"
    
    @classmethod
    def getTotalContas(cls):
        return cls.__totalContas
    
    @property
    def saldo(self):
          return self.__saldo
    @saldo.setter
    def saldo(self,valor):
        if(valor<0):
            print("Saldo Invalido!!!")
        else:
            self.__saldo = valor
               
    def __init__(self,numero,cpf,nomeTitular,saldo):
        self.__numero = numero 
        self.__cpf = cpf
        self.__nomeTitular = nomeTitular
        self.__saldo = saldo
        type(self).__totalContas+=1
    
    def depositar(self,valor):
        self.__saldo = self.saldo+valor
        
    def sacar(self,valor):
        if self.__saldo < valor:
            return False
        else: 
            self.__saldo = self.saldo-valor
            return True
        
    def gerarExtrato(self):
        print("="*20,"EXTRATO BANCARIO","="*20)
        print(f"Nome do Titular: {self.__nomeTitular}")
        print(f"CPF: {self.__cpf}")
        print(f"Numero da Conta: {self.__numero}")
        print(f"Saldo: {self.__saldo}")
        print("="*58)
    
    def tranfereValor(self,contaDestino,valor):
        if self.__saldo <valor:
            return("Saldo Insuficiente")
        else:
            contaDestino.depositar(valor)
            self.__saldo = self.__saldo - valor
            return("Tranferencia Realizada com Sucesso!!!")
        
  
"""conta1 = Conta(1,13156,"Marcos",1500)
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
"""
        