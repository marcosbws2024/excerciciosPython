from Classes.Banco import Banco
from Classes.ContaVip import ContaVip
from Classes.ContaComum import ContaComum


banco1 = Banco(999,"Teste")
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contavip1 = ContaVip(2,0.01,0.1,2000,0.05)

banco1.adicionaConta(contacomum1)
banco1.adicionaConta(contavip1)
banco1.calcularRendimentoMensal()
banco1.imprimeSaldoContas()