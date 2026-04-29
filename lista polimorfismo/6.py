from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio:float = raio
        
    def calcular_area(self):
        area = pi * self.raio * self.raio
        return f'Area do circulo eh igual a {area}'

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura:float = largura
        self.altura:float = altura
    
    def calcular_area(self):
        area = self.largura * self.altura
        return f'Area do retangulo eh igual a {area}'

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base:float = base
        self.altura:float = altura
    
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return f'Area do triangulo eh igual a {area}'

formas = [Circulo(15), Retangulo(30, 10), Triangulo(15, 30)]
for forma in formas:
    print(forma.calcular_area())