class Motor:
    def __init__(self, potencia):
        self.potencia:int = potencia
        self.motor = 'combustao'

    def ligar(self):
        print(f"Motor a {self.motor} ligado em {self.potencia} potencia")


class MotorEletrico(Motor):
    def __init__(self, potencia):
        super().__init__(potencia)
        self.motor:str = 'energia'
    
    def ligar(self):
        print(f"Motor a {self.motor} ligado em {self.potencia} potencia")
    

# -------------------------------------------

class Carro:
    def __init__(self, modelo, motor):
        self.modelo:str = modelo
        self.motor = motor

    def ligar_carro(self):
        print(f"{self.modelo} ligando..")

class CarroEletrico(Carro):
    def __init__(self, modelo, motor):
        super().__init__(modelo, motor)
        self.motor = MotorEletrico(motor)

m = Motor(1200)
m.ligar()
c = Carro("Fusca", m)
c.ligar_carro()

print("\n-----------------\n")

me = MotorEletrico(1500)
me.ligar()
ce = CarroEletrico("Geely", me)
ce.ligar_carro()