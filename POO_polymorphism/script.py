class Vehicule:
    def avance(self):
        print("Le véhicule démarre")


class Voiture(Vehicule):
    def avance(self):
        super().avance()            # Polymorphisme : On appelle la méthode parent et on l'augmente
        print("La voiture roule")


class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")


v = Voiture()
a = Avion()
v.avance()
a.avance()
