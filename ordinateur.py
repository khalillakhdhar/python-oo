#class ordinateur: cpu,ram,marque, prixunitaire,
class Ordinateur:
    def __init__(self,cpu,ram,marque,prixunitaire): #constructeur de la classe
        self.cpu=cpu
        self.ram=ram
        self.marque=marque
        self.prixunitaire=prixunitaire
        # self est un mot clé qui fait référence à l'objet lui-même
    def calculeTva(self):
        return self.prixunitaire*0.19
    def affiche(self):
        #affichage sur une seule ligne formatée
        print("cpu:",self.cpu,"ram:",self.ram,"marque:",self.marque,"prixunitaire:",self.prixunitaire,"TVA:",self.calculeTva())
