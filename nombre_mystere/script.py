import random

random_nb = random.randint(0, 100)
attempt = 6
try_nb = 0

print("*** 🤔 Jeux du nombre mystère 🤔 ***")

while attempt != 0:
    print(f"Il te reste {attempt} essai{'s' if attempt > 1 else ''}")
    
    nb_choosen = input("Choisissez un nombre entre 0 et 100 : ")

    if nb_choosen.isdigit() == False:
        print("Veuillez rentrer un nombre 😅")
        continue

    nb_choosen = int(nb_choosen)

    try_nb += 1
    attempt -= 1

    if nb_choosen > random_nb:
        if attempt != 0:
            print(f"Loupé ! Le nombre est plus petit que {nb_choosen}")
        else:
            print('Loupé !')
    
    elif nb_choosen < random_nb:
        if attempt != 0:
            print(f"Loupé ! Le nombre est plus grand que {nb_choosen}")
        else:
            print('Loupé !')
    
    else:
        print(f"C'est bien le nombre {random_nb} !")
        if try_nb == 1:
            print(f"Félicitation ! Vous avez trouvé en {try_nb} essai 😃")
        else:
            print(f"Félicitation ! Vous avez trouvé en {try_nb} essais 😃")
        break

    if attempt == 0:
        print("Tu n'as plus d'essai...")
        print(f"Le nombre à deviner était : {random_nb}")

if nb_choosen != random_nb:
    print("Tu as perdu... 😢")

print("Fin du jeu, à bientôt ! 👋")
