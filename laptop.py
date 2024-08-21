# laptop hérite de la classe ordinateur dans ordinateur.py
#laptop à un attribut supplémentaire: autonomie
from ordinateur import Ordinateur
class Laptop(Ordinateur):
    def __init__(self,cpu,ram,marque,prixunitaire,autonomie):
        super().__init__(cpu,ram,marque,prixunitaire)
        self.autonomie=autonomie
    #polymorphisme de la méthode affiche
    def affiche(self):
        super().affiche()
        print("autonomie:",self.autonomie)
    #polymorphisme de la méthode calculeTva
    def calculeTva(self):
        return super().calculeTva()+self.prixunitaire*0.12
    