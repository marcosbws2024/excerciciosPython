class ContaEncapsulamento:
    def __init__(self, numero, saldo):
        self.__numero = numero #o underline indica atributo privado
        self.__saldo = saldo #o underline indica atributo privado

def main():
    conta1 = ContaEncapsulamento("0101", 1000)
    saldo =conta1.saldo
    print(saldo)

if __name__ == "__main__":
    main()