from abc import ABC, abstractmethod

class dispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class carregavel(ABC):
    @abstractmethod
    def carregar(self):
        pass




class smartphone(dispositivoEletronico,carregavel):
    def carregar(self):
        return "celular carregando"
    def desligar(self):
        return "celular desligando"
    def ligar(self):
        return "celular ligando"



class notebook(dispositivoEletronico,carregavel):
   def carregar(self):
        return "pc carregando"
   def desligar(self):
        return "pc desligando"
   def ligar(self):
        return "pc ligando"





class fone(dispositivoEletronico):
    
     def desligar(self):
        return "fone desligando"
     def ligar(self):
        return "fone ligando"














if __name__ == "__main__":
    
    dispositivos = [
        smartphone(),
        notebook(),
        fone()
    ]

    carregaveis = [
        smartphone(),
        notebook()
    ]

    print("=== Dispositivos Eletrônicos ===")
    for dispositivo in dispositivos:
        print(dispositivo.ligar())
        print(dispositivo.desligar())

    print("\n=== Dispositivos Carregáveis ===")
    for dispositivo in carregaveis:
        print(dispositivo.carregar())