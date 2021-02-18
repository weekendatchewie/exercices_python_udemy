class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod  # decorator, methode de classe
    def lamborghini(cls):  # 'cls' paramètre qui représente la classe
        return cls(marque="Lamborghini", vitesse=50, prix=200)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=40, prix=180)

    @classmethod
    def ford(cls):
        return cls(marque="Ford", vitesse=30, prix=160)


# On utilise les méthode pour créer des instances plutôt que de toujours réécrire les paramètres
lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
