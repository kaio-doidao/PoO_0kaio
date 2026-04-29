class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def ligar_motor(self):
        print(f"Ligando motor a {self.potencia} cv")
    
    def exibir_info(self):
        print(f"Motor de {self.potencia} cv")

class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria
    
    def carregar(self):
        print("Carregando bateria...")
    
    def exibir_info(self):
        print(f"Bateria de {self.bateria} quilowatts/h")
    
class Combustao:
    def __init__(self, tanque):
        self.tanque = tanque
    
    def abastecer(self):
        print("Abastecendo tanque...")
    
    def exibir_info(self):
        print(f"Tanque abastecido com {self.tanque} litros")

# -------------------------------------------

class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)
    
    def exibir_info(self):
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)

class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)
        Combustao.__init__(self, tanque)

    def exibir_info(self):
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)
    
ce = CarroEletrico(1200, 70)
ch = CarroHibrido(1500, 60, 14)
print("Carro Híbrido:")
ch.carregar()
ch.abastecer()
ch.ligar_motor()

print("----------------")

ch.exibir_info()

print("\n")
print("Carro Eletrico:")
ce.carregar()
ce.ligar_motor()

print("----------------")

ce.exibir_info()