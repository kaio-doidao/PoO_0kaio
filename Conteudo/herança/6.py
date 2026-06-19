class Nadador:
    def mover(self):
        print("kaio esta nadando e parou no meio da piscina")
    
class Corredor:
    def mover(self):
        print("kaio esta correndo")

class Triatleta(Nadador, Corredor):
    def mover(self):
        Corredor.mover(self)
        Nadador.mover(self)

t = Triatleta()
t.mover()