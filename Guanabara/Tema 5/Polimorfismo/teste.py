from Classes.Banco import Banco
from Classes.ContaCliente import ContaCliente
from Classes.ContaComum import ContaComum
from Classes.ContaRemunerada import ContaRemunerada

banco1 = Banco(999,"Teste")
contaCliente1 = ContaCliente(1,0.01,0.1,2000,0.05)
contaComum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaRemunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaConta(contaCliente1)
banco1.adicionaConta(contaComum1)
banco1.adicionaConta(contaRemunerada1)
banco1.calcularRendimentoMensal()
banco1.imprimeSaldoContas()