class Animal:
    def __init__(self):
        self.grupo:str = ''
    
class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        self.grupo:str = 'mamifero'
    