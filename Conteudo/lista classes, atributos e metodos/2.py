class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print("Marca", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)

# exemplo
carro = Carro("toyota", "Corolla", 2020)
carro.exibir_dados()