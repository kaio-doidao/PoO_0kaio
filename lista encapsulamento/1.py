class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor indisponivel para depositar")

    def sacar(self, valor):
        if self.__saldo > valor:
            self.__saldo -= valor
        else:
            print(f"Voce nao tem saldo o suficiente, seu saldo eh de: R${self.__saldo}")
   
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")
   


conta = ContaBancaria("Maria", 0)
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()
