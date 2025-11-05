from Conta import Conta
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo) #inicia atributos heradados da classe conta
        self.limite = limite

#polimorfismo, fazendo um sacar proprio que permite o limite negativo

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente conta numero {self.numero} cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

        #metodo depositar deve ser reescrito, pois primeiro sai do limite negativo até chegar no positivo
