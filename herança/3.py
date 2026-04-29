class Animal:
    def __init__(self):
        self.nome:str = ''

    def fazer_som(self):
        print("Som de um animal")

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.grupo = 'mamífero'

    def fazer_som(self):
        print("Latido")