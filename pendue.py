import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définition de la taille de la fenêtre
largeur, hauteur = 800, 600
taille_texte = 40

# Chargement de la police
police = pygame.font.SysFont(None, taille_texte)

# Fonction pour choisir un mot aléatoire dans le fichier mots.txt
def choisir_mot():
    with open("mots.txt", "r") as fichier:
        mots = fichier.readlines()
    return random.choice(mots).strip()

# Fonction pour ajouter un mot au fichier mots.txt
def ajouter_mot(nouveau_mot):
    with open("mots.txt", "a") as fichier:
        fichier.write("\n" + nouveau_mot)

# Fonction pour afficher le mot avec les lettres devinées
def afficher_mot(mot, lettres_trouvees):
    mot_affiche = ''
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + ' '
        else:
            mot_affiche += '_ '
    return mot_affiche

# Fonction principale du jeu
def pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    lettres_devinees = set()
    chances = 7

    print("Bienvenue dans le jeu du pendu!")
    print("Essayez de deviner le mot.")

    while chances > 0:
        mot_affiche = afficher_mot(mot_a_deviner, lettres_trouvees)
        print(mot_affiche)

        if '_' not in mot_affiche:
            print("Félicitations! Vous avez deviné le mot!")
            break

        print(f"Chances restantes : {chances}")
        lettre = input("Devinez une lettre: ").lower()

        if lettre == "ajouter":
            nouveau_mot = input("Entrez un nouveau mot à ajouter: ").lower()
            ajouter_mot(nouveau_mot)
            print(f"Le mot '{nouveau_mot}' a été ajouté au fichier mots.txt.")
            continue

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_devinees.add(lettre)

        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print(f"Bonne devinette! '{lettre}' est dans le mot.")
        else:
            chances -= 1
            print(f"Dommage! La lettre '{lettre}' ne fait pas partie du mot.")

    else:
        print(f"Dommage! Le mot était '{mot_a_deviner}'.")

# Lancer le jeu
pendu()

# Fermeture de Pygame
pygame.quit()