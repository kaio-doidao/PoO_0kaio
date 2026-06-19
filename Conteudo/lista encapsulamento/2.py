class Estudante:
    def __init__(self, id, nome):
        self.__id = id
        self.nome = nome
        self.__creditos = 1

    @property
    def id(self):
        return self.__id
    
    @property
    def creditos(self):
        return self.__creditos


    @creditos.setter
    def creditos(self,valor):
        if valor <= 0:
            self._creditos = 1
        else:
            self.__creditos = valor


    def detalhar(self):
        print("Id:", self.__id)
        print("Nome:", self.nome)
        print("Creditos:", self.__creditos)




e1 = Estudante(20251174010072, "Vitor")
e2 = Estudante(20251174010003, "Helia")
e1.creditos = -3
e2.creditos = 2
e1.detalhar()
e2.detalhar()