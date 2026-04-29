class Cidade:
    def __init__(self, nome):
        self.nome:str = nome

    def __str__(self):
        return f"Cidade: {self.nome}"

class Pessoa:
    def __init__(self, nome, cidade):
        self.nome:str = nome 
        self.cidade = cidade

    def __str__(self):
        return f"Nome: {self.nome}, {self.cidade}"

class Animal:
    def __init__(self, nome, dono):
        self.nome:str = nome 
        self.pessoa = dono

    def __str__(self):
        return f"Nome: {self.nome}, {self.pessoa}"

c = Cidade("Natal")
p = Pessoa("Vitor", c)
a = Animal("j", p)
print(c)
print(p)
print(a)