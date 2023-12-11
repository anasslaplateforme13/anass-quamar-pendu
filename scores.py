import random

mots = ['pendu', 'jeu', 'programmation', 'ordinateur', 'apprentissage',
        'algorithme', 'developpement', 'intelligence', 'programme', 'connaissance',
        'informatique', 'technologie', 'logiciel', 'web']

def choisir_mot():
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre + " "
        else:
            mot_cache += "_ "
    return mot_cache

def deviner_mot():
    mot_a_deviner = choisir_mot().upper()
    lettres_trouvees = []
    max_erreurs = 6
    erreurs = 0
    score = 0

    print("Bienvenue dans le jeu du pendu!")
    print("Devinez le mot en moins de 6 erreurs.")
    print(afficher_mot_cache(mot_a_deviner, lettres_trouvees))

    while True:
        proposition = input("Entrez une lettre ou devinez le mot: ").upper()

        if proposition == mot_a_deviner:
            score += 10
            print("Félicitations! Vous avez deviné le mot:", mot_a_deviner)
            print(f"Votre score est de {score} points.")
            break

        if len(proposition) == 1 and proposition.isalpha():
            if proposition in lettres_trouvees:
                print("Vous avez déjà deviné cette lettre.")
            elif proposition in mot_a_deviner:
                lettres_trouvees.append(proposition)
                print("Bonne devinette!")
                mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
                print(mot_cache)
                if "_ " not in mot_cache:
                    score += 5
                    print("Félicitations! Vous avez deviné le mot:", mot_a_deviner)
                    print(f"Votre score est de {score} points.")
                    break
            else:
                erreurs += 1
                print("Lettre incorrecte.")
                print(f"Erreurs restantes : {max_erreurs - erreurs}")
                if erreurs == max_erreurs:
                    print("Vous avez atteint le nombre maximum d'erreurs. Le mot était:", mot_a_deviner)
                    print(f"Votre score est de {score} points.")
                    break
        else:
            print("Veuillez entrer une lettre valide ou devinez le mot.")

deviner_mot()
