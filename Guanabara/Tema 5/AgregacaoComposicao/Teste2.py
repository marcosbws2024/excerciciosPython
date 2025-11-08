from Classes.Conta2 import Conta2

c1 = Conta2(1,100,"marcos",500)
c2 = Conta2(1,100,"maria",1500)
c3 = Conta2(1,100,"john",1500)
c1.sacar(2000)
c1.saldo = 1500 
#c1._Conta2__saldo=-8000
#c1.gerarExtrato()
#c1.saldo= -1500


print(f"Conta 1: {c1.saldo}")
print(f"Conta 2: {c2.saldo}")
print(f"Foram criadas {Conta2.getTotalContas()} Contas")
print(f"Obrigado por fazer parte do {Conta2.nomeBanco()}")