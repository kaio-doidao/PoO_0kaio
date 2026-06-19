class ContaCorrente:
    def __init__(self, nome_correntista, cpf_correntista, saldo):
        self.nome_correntista = nome_correntista
        self.cpf_correntista = cpf_correntista
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print("Nome:", self.nome_correntista)
        print("Cpf:", self.cpf_correntista)
        print("Saldo:", self.saldo)


corrente = ContaCorrente("helia", "77801537808", 1200)
corrente.depositar(300)
corrente.sacar(150)
corrente.mostrar_saldo()