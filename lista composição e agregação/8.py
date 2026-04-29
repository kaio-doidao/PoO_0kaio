class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"
    
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_livros = []

    def adicionar_livros(self, livro):
        self.lista_de_livros.append(livro)

    def listar_livros(self):
        print(f"Livros da {self.nome}:")
        for livros in self.lista_de_livros:
            print(livros)

livro1 = Livro("A droga da obediencia", "Pedro Bandeira")
livro2 = Livro("Sonho de uma noite de verao", "William Shakespeare")
bib = Biblioteca("Biblioteca encanto")
bib.adicionar_livros(livro1)
bib.adicionar_livros(livro2)
bib.listar_livros()