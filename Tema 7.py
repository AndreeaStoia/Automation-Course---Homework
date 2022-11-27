'''ABSTRACTION
Clasa abstractă FormaGeometrica
- Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica. Constructor pentru latură.

ENCAPSULATION
- latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI=3.14
    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(self):
        print(f"Cel mai probabil am colturi.")

class Patrat(FormaGeometrica):
    __latura = 0
    def __init__(self,latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f"Latura actuala este de: {self.__latura}")
        return self.__latura

    @latura.setter
    def latura(self,latura):
        self.__latura = latura
        print(f"Noua latura este de: {latura}.")

    @latura.deleter
    def latura(self):
        self.__latura = None
        print(f"Am sters valoarea laturii.")

    def aria(self):
        aria = self.__latura ** 2
        print(f"Aria patratului este de {aria}.")

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f"Raza actuala este de: {self.__raza}")
        return self.__raza

    @raza.setter
    def raza(self,raza):
        self.__raza = raza
        print(f"Noua raza este de: {raza}.")

    @raza.deleter
    def raza(self):
        self.__raza = None
        print(f"Am sters valoarea razei.")

    def aria(self):
        aria = self.PI * self.__raza ** 2
        print(f"Aria cercului este de {aria}.")

    def descrie(self):
        print("Eu nu am colturi.")

patrat1 = Patrat(10)
patrat1.latura        #getter
patrat1.latura = 5    #setter
del patrat1.latura    #deleter
patrat1.latura = 7
patrat1.aria()
patrat1.descrie()
print("-----------------------------")
cerc1 = Cerc(9)
cerc1.raza            #getter
cerc1.raza = 5        #setter
del cerc1.raza        #deleter
cerc1.raza = 6
cerc1.aria()
cerc1.descrie()



