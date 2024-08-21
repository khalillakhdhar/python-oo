# classe abstraite des animeaux avec une méthode abstraite faireDuBruit
class Animal:
    #nom, poids, age, sexe, couleur
    def __init__(self,nom,poids,age,sexe,couleur):
        self.nom=nom
        self.poids=poids
        self.age=age
        self.sexe=sexe
        self.couleur=couleur
    def bouger(self, distance):
        print(self.nom,"se déplace de",distance,"mètres")
    def faireDuBruit(self):
        pass
    def affiche(self):
        print("nom:",self.nom,"poids:",self.poids,"age:",self.age,"sexe:",self.sexe,"couleur:",self.couleur,"bruit:",self.faireDuBruit())