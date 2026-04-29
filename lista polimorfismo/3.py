class Animal:
    def emitir_som(self):
        return 'Algum som generico'

class Cachorro:
    def emitir_som(self):
        return 'Latido'

class Gato(Animal):
    def emitir_som(self):
        som = super().emitir_som()
        print(f"{som}")
        return 'Miau'

animais = [Animal(), Cachorro(), Gato()]
for animal in animais:
    print(animal.emitir_som())