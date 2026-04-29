class Forma:
    def area(self):
        return 0

class Retangulo(Forma):
    def area(self, largura, altura):
        retangulo = largura * altura
        return f'{retangulo}'
    