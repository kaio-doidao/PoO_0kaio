class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def __str__(self):
        return f"Motor de {self.potencia} cavalos ligado."

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo 
        self.motor = motor 

    def __str__(self):
        return f"Ligando o {self.modelo}..."

m = Motor(200)
c = Carro("Toyota", m)
print(m)
print(c)