class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    @property
    def get__saldo(self):
        return self.__saldo

    @get__saldo.setter
    def set_saldo(self, valor):
        if valor < 0:
            print("Saldo indisponivel")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor indisponivel para depositar")

    def sacar(self, valor):
        if valor < 0:
            print("Valor indisponivel para saque")
        else:
            self.__saldo -= valor

minha_conta = ContaBancaria("maria")
minha_conta.depositar(500)
minha_conta.sacar(200)
print(f"Saldo: {minha_conta.get__saldo}")
minha_conta.set_saldo = 250
print(f"Saldo: {minha_conta.get__saldo}")