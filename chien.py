#chien héritant la classe animal
from animal import Animal
class Chien(Animal):
    def __init__(self,nom,poids,age,sexe,couleur,puce):
        super().__init__(nom,poids,age,sexe,couleur)
        self.puce=puce
    def faireDuBruit(self):
        print("ouaf ouaf")
    def affiche(self):
        super().affiche()
        print("puce:",self.puce)