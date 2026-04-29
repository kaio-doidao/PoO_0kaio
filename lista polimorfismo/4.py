class Animal:
    def emitir_som(self):
        return 'Algum som generico'

class Cachorro(Animal):
    def emitir_som(self):
        return 'Latido'

class Gato(Animal):
    def emitir_som(self):
        return 'Miau'

animais = [Animal(), Cachorro(), Gato()]
for animal in animais:
    print(animal.emitir_som())