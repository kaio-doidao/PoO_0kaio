from abc import ABC, abstractmethod


class Controlavel(ABC):
    @abstractmethod
    def mover(self):
        pass

class Jogador(Controlavel):
    def mover(self):
        print("Jogador se movendo")

class Volante(Controlavel):
    def mover(self):
        print("Volante girando")


jogador = Jogador()
volante = Volante()
jogador.mover()
volante.mover()