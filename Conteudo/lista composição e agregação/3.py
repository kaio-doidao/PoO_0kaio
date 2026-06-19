class Autor:
    def __init__(self, autor):
        self.autor = autor 

    def __str__(self):
        return f"Autor: {self.autor}"

class Livro:
    def __init__(self, livro, autor):
        self.livro = livro
        self.autor = autor 

    def __str__(self):
        return f"Nome do livro: {self.livro}, {self.autor}"

autor = Autor("Pedro Bandeira")
livro = Livro("A droga da obediencia", autor)
print(autor)
print(livro)