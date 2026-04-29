class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Meu nome é", self.nome)

p1 = Pessoa("Ana", 20)
p1.apresentar()