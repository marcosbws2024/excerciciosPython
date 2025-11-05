#Burlando atributos privados 
#pihton não possui atributos privados reais

from Classes.Conta import Conta

conta1 = Conta(1,100)
saldo1 = conta1._Conta__saldo
print(saldo1)

saldo2= conta1.saldo
