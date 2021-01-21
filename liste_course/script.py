
liste_course = []

option_liste = ""

while not option_liste == "5":

    print("Choisissez entre les options suivantes : ")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    
    option_liste = input("Votre choix : ")

    if option_liste == "1":
        item_liste = input("Ajouter un élément à la liste : ")
        liste_course.append(item_liste)

    elif option_liste == "2":
        item_remove = input("Sélectionnez l'élément à supprimer : ")
        liste_course.remove(item_remove)

    elif option_liste == "3":
        print(liste_course)

    elif option_liste == "4":
        del liste_course[::-1]

    elif option_liste == "5":
        print("A bientôt !")

    else:
        print("Options pas valides")
        

# ======================== SOLUTION DONNÉE DE L'EXERCICE ================================

# LISTE = []

# MENU = """Choisissez parmi les 5 options suivantes :
# 1: Ajouter un élément à la liste
# 2: Retirer un élément de la liste
# 3: Afficher la liste
# 4: Vider la liste
# 5: Quitter
# ? Votre choix : """

# MENU_CHOICES = ["1", "2", "3", "4", "5"]


# while True:
#     user_choice = input(MENU)
#     if user_choice not in MENU_CHOICES:
#         print("Veuillez choisir une option valide...")
#         continue

#     if user_choice == "1":  # Ajouter un élément
#         item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
#         LISTE.append(item)
#         print(f"L'élément {item} a bien été ajouté à la liste.")
#     elif user_choice == "2":  # Retirer un élément
#         item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
#         if item in LISTE:
#             LISTE.remove(item)
#             print(f"L'élément {item} a bien été supprimé de la liste.")
#         else:
#             print(f"L'élément {item} n'est pas dans la liste.")
#     elif user_choice == "3":  # Afficher la liste
#         if LISTE:
#             print("Voici le contenu de votre liste :")
#             for i, item in enumerate(LISTE, 1):
#                 print(f"{i}. {item}")
#         else:
#             print("Votre liste ne contient aucun élément.")
#     elif user_choice == "4":  # Vider la liste
#         LISTE.clear()
#         print("La liste a été vidée de son contenu.")
#     elif user_choice == "5":  # Quitter
#         print("À bientôt !")
#         sys.exit()

#     print("-" * 50)
