class Comodo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome}, {self.tamanho}"

class Casa:
    def __init__(self):
        self.lista_de_comodos = []

    def adicionar_comodo(self, comodo):
        self.lista_de_comodos.append(comodo)

    def listar_comodos(self):
        print("Comodos:")
        for comodo in self.lista_de_comodos:
            print(comodo)

comodo1 = Comodo("Cozinha", "5 x 5")
comodo2 = Comodo("Sala", "3 x 3")
casa = Casa()
casa.adicionar_comodo(comodo1)
casa.adicionar_comodo(comodo2)
casa.listar_comodos()