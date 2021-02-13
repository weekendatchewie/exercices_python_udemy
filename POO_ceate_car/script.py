class Voiture:

    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence}L d'essence")

    def drive(self, km):
        self.essence -= (km * 5) / 100

        if 0 < self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")

        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            self.essence = 0
            return
        else:
            self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")
