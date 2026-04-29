class Processador:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    
    def __str__(self):
        return f"Modelo: {self.modelo}, Velocidade: {self.velocidade}GHz"
    
class Memoria:
    def __init__(self, capacidade):
        self.capacidade = capacidade

    def __str__(self):
        return f"Capacidade da memoria: {self.capacidade}gb"

class Computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria
    
    def exibir_configuraçao(self):
        print(f"{self.processador} - {self.memoria}")

proc = Processador("AMD ryzen 7 7735hz", 3.20)
mem = Memoria(512)
comp = Computador(proc, mem)
comp.exibir_configuraçao()
