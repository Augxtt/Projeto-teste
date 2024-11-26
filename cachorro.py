from animal import Animal
class Cachorro(Animal):
    def __init__ (self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte

    def setPorte(self, porte):
        self.__porte = porte
    def getPorte(self):
        return self.__porte
    def mostrar(self):
        return (f"Nome do cachorro é {self.getNome()}, o cachorro possui {self.getIdade()} anos de idade e é um cachorro de porte {self.getPorte()}")
    
#a = Cachorro("thor", 3 ,"médio")
#print(a.mostrar())