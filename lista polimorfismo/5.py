class Veiculo:
    def mover(self):
        return 'Veiculo esta se movendo'

class Carro(Veiculo):
    def mover(self):
        return 'Carro acelerando'

class Moto(Veiculo):
    def mover(self):
        return 'Moto empinando'

class Bicicleta(Veiculo):
    def mover(self):
        return 'Bicicleta pedalando'

veiculos = [Veiculo(), Carro(), Moto(), Bicicleta()]
for veiculo in veiculos:
    print(veiculo.mover())