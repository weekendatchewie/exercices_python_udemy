class Voiture:
    voiture_crees = 0

    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    # '__str__' permet d'afficher ce que l'on souhaite lorsque l'on print notre instance, ou qu'on la convertie en str
    def __str__(self):
        return f"La marque de la voiture est {self.marque}, d'une vitesse de {self.vitesse}km/s, et le prix est de {self.prix} ecus"

    @classmethod  # decorator, methode de classe
    def lamborghini(cls):  # 'cls' paramètre qui représente la classe
        return cls(marque="Lamborghini", vitesse=50, prix=200)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=40, prix=180)

    @classmethod
    def ford(cls):
        return cls(marque="Ford", vitesse=30, prix=160)

    @staticmethod
    def afficher_voiture():
        if Voiture.voiture_crees <= 1:
            print(f"Il y a {Voiture.voiture_crees} voiture")
        else:
            print(f"Il y a {Voiture.voiture_crees} voitures")


# On utilise les méthode pour créer des instances plutôt que de toujours réécrire les paramètres
lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_voiture()
print(lambo)
