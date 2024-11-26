from animal import Animal
class Gato(Animal):
    def __init__ (self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def setRaca(self, raca):
        self.__raca = raca
    def getRaca (self):
        return self.__raca
    def mostrar(self):
        return (f"O nome do gato é {self.getNome()}, possui {self.getIdade()} anos de idade e pertence a raça {self.getRaca()}")
    
#g = Gato("caramelo", 4 ,"laranja")
#print(g.mostrar())