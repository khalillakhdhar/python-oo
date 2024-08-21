# chat héritant la classe animal et definissant la methode faireDuBruit
from animal import Animal
class Chat(Animal):
    def __init__(self,nom,poids,age,sexe,couleur,collier):
        super().__init__(nom,poids,age,sexe,couleur)
        self.collier=collier
    def faireDuBruit(self):
        print("miaou")
    def affiche(self):
        super().affiche()
        print("collier:",self.collier)