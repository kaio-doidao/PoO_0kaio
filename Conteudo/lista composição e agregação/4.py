class Jogador:
    def __init__(self, nome, posiçao):
        self.nome = nome
        self.posiçao = posiçao
    
    def __str__(self):
        return f"{self.nome}, {self.posiçao}"

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_jogadores = []
    
    def adicionar_jogador(self, jogador):
        self.lista_de_jogadores.append(jogador)
    
    def listar(self):
        print(f"{self.nome}")
        for jogadores in self.lista_de_jogadores:
            print(jogadores)

jogador1 = Jogador("Neymar", "Goleiro")
jogador2 = Jogador("Vinijr", "Atacante")
time = Time("Brasil")
time.adicionar_jogador(jogador1)
time.adicionar_jogador(jogador2)
time.listar()