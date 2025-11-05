
from Cliente import Cliente
from contaClienteExtrato import Conta

cliente1 =  Cliente(123,"João","rua 1")
cliente2 =  Cliente(345,"Maria","rua 2")

conta1 = Conta([cliente1,cliente2],1,0)

conta1.gerarsaldo()
conta1.depositar(1500)
conta1.gerarsaldo()
conta1.sacar(500)
conta1.gerarsaldo()
