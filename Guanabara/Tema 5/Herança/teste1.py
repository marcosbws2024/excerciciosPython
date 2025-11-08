from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.ContaEspecial import ContaEspecial

cliente1 = Cliente("123","joão", "Rua X")
cliente2 = Cliente("123","joana", "Rua X")
cliente3 = Cliente("456","Ze","Rua X")

conta1 = Conta(cliente1,1,2000)
conta2 = Conta(cliente2,2,2000)
conta3 = ContaEspecial(cliente3,3,2000,1000)

conta1.depositar(300)
conta1.tranfereValor(conta2,500)
conta3.depositar(600)
conta1.gerarSaldo()
conta2.gerarSaldo()
conta2.sacar(200)
conta2.sacar(700)
conta3.sacar(900)

conta1.extrato.gerarExtrato(conta1.numero)
conta2.extrato.gerarExtrato(conta2.numero)
conta3.extrato.gerarExtrato(conta3.numero)
conta3.sacar(1800)

conta1.gerarSaldo()
conta2.gerarSaldo()
conta3.sacar(2600)
conta3.gerarSaldo()