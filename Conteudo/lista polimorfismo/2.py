class Animal:
    def emitir_som(self):
        return 'Algum som generico'

class Cachorro:
    def emitir_som(self):
        return 'Latido'

class Gato:
    def emitir_som(self):
        return 'Miado'

animais = [Animal(), Cachorro(), Gato()]
for animal in animais:
    print(animal.emitir_som())