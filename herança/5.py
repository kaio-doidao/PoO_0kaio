class Funcionario:
    def __init__(self, nome, salario):
        self.nome:str = nome
        self.salario:int = salario
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}, salario: R${self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)  
        self.bonus:int = bonus

    def exibir_dados(self):
        print(f"Nome: {self.nome}, salario: R${self.salario} + Bonus de R${self.bonus}")
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Linguagem de programação utilizada: {self.linguagem} , salario: R${self.salario}")

gerente = Gerente("Vitor", 12200, 3000)
desenvolvedor = Desenvolvedor("Helia", 7500, "Python")
gerente.exibir_dados()
desenvolvedor.exibir_dados()