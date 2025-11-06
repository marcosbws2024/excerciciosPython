# A importação deve funcionar seguindo a estrutura: Pasta.Arquivo import Classe
from Classes.Cliente import Cliente
from Classes.Conta import Conta


# Testando o codigo
c1 = Cliente("123","Marcelo","Estrada1")
c2 = Cliente("456","Marcia","Estrada2")

conta1 = Conta([c1,c2],111,1500)
conta1.depositar(1200)
conta1.sacar(200)
conta1.extrato.gerarExtrato(conta1.numero)

