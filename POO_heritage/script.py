projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]


class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)  # La fonction 'super' récupère les méthodes de la classe parente

    # On utilise la surcharge pour modifier la méthode quand elle est appelée par la classe 'Junior'
    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)


paul = Junior("Paul", "Durand")
paul.afficher_projets()
