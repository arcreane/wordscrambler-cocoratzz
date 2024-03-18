# Importez le module tkinter
# import tkinter as tk
# import random
# import string

# difficulty_dic = {
#     "a": ("Easy", 10, 5, (2, 3)),
#     "b": ("Medium", 15, 7, (4, 6)),
#     "c": ("Hard", 30, 15, (6, 9))
# }

# def generer_lettre_aleatoire():
#     return random.choice(string.ascii_uppercase)

# def generer_mot_aleatoire(taille_min, taille_max):
#     longueur = random.randint(taille_min, taille_max)
#     return ''.join(random.choices(string.ascii_uppercase, k=longueur))

# def creer_grille(fenetre, lignes, colonnes):
#     grille = [[None] * colonnes for _ in range(lignes)]
#     for i in range(lignes):
#         for j in range(colonnes):
#             lettre = generer_lettre_aleatoire()
#             cellule = tk.Label(fenetre, text=lettre, borderwidth=1, relief="solid", width=5, height=2)
#             cellule.grid(row=i, column=j)
#             grille[i][j] = cellule
#     return grille

# def placer_mots_dans_grille(grille, mots):
#     for mot in mots:
#         taille_mot = len(mot)
#         if taille_mot <= len(grille) and taille_mot <= len(grille[0]):
#             direction = random.choice(['horizontal', 'vertical'])
#             if direction == 'horizontal':
#                 debut_ligne = random.randint(0, len(grille) - 1)
#                 debut_colonne = random.randint(0, len(grille[0]) - taille_mot)
#                 for i in range(taille_mot):
#                     grille[debut_ligne][debut_colonne + i].config(text=mot[i])
#             else:
#                 debut_ligne = random.randint(0, len(grille) - taille_mot)
#                 debut_colonne = random.randint(0, len(grille[0]) - 1)
#                 for i in range(taille_mot):
#                     grille[debut_ligne + i][debut_colonne].config(text=mot[i])

# def play_a_new_game():
#     user_choice = input("""Select your difficulty:
#      a. Easy - words less than 4 letters, grid size: 10x5
#      b. Medium - words between 4 and 6 letters, grid size: 15x7
#      c. Hard - words between 6 and 9 letters, grid size: 30x15
#      2. for quit
#     """)
#     if user_choice == "a":
#         creer_et_afficher_grille(*difficulty_dic["a"])
#     elif user_choice == "b":
#         creer_et_afficher_grille(*difficulty_dic["b"])
#     elif user_choice == "c":
#         creer_et_afficher_grille(*difficulty_dic["c"])
#     elif user_choice == "2":
#         exit()
#     else:
#         print("Invalid choice. Please choose again.")
#         play_a_new_game()

# def creer_et_afficher_grille(difficulty, lignes, colonnes, longueur_mots):
#     fenetre = tk.Tk()
#     fenetre.title("Grille de mots mêlés")

#     grille = creer_grille(fenetre, lignes, colonnes)
#     mots = [generer_mot_aleatoire(*longueur_mots) for _ in range(10)]
#     placer_mots_dans_grille(grille, mots)

#     Pour suivre les mots trouvés
#     mots_trouves = set()  

#     while len(mots_trouves) < len(mots):
#         Demander à l'utilisateur d'entrer le mot, les coordonnées de la première lettre et la direction
#         mot = input("Entrez le mot que vous pensez avoir trouvé (ou entrez 'exit' pour quitter) : ")
#         if mot.lower() == "exit":
#             break
#         coord_x = int(input("Entrez la coordonnée x de la première lettre : "))
#         coord_y = int(input("Entrez la coordonnée y de la première lettre : "))
#         direction = input("Entrez la direction (horizontal, vertical) : ")

#         Vérifier si le mot correspond aux lettres dans la grille en fonction des coordonnées et de la direction
#         mot_trouve = True
#         if direction == 'horizontal':
#             for i in range(len(mot)):
#                 if grille[coord_x][coord_y + i].cget("text") != mot[i]:
#                     print("Le mot ne correspond pas.")
#                     mot_trouve = False
#                     break
#             else:
#                 print("Le mot a été trouvé horizontalement !")
#         elif direction == 'vertical':
#             for i in range(len(mot)):
#                 if grille[coord_x + i][coord_y].cget("text") != mot[i]:
#                     print("Le mot ne correspond pas.")
#                     mot_trouve = False
#                     break
#             else:
#                 print("Le mot a été trouvé verticalement !")

#         if mot_trouve:
#             mots_trouves.add(mot)

#     Vérifier si tous les mots ont été trouvés
#     if len(mots_trouves) == len(mots):
#         print("Félicitations ! Vous avez trouvé tous les mots !")

#     fenetre.mainloop()

# Lancement du jeu
# play_a_new_game()

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

# Charger les mots français depuis un fichier texte
def charger_mots_francais():
    # Cette fonction charge les mots français à partir d'un fichier texte.
    with open("words.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Générer un mot aléatoire à partir de la liste de mots français chargés
def generer_mot_aleatoire(mots_fr, taille_min, taille_max):
    # Cette fonction génère un mot aléatoire en fonction de la taille spécifiée.
    mots_filtres = [mot for mot in mots_fr if taille_min <= len(mot) <= taille_max]
    return random.choice(mots_filtres)

# Fonction pour créer la fenêtre de démarrage du jeu
def creer_fenetre_demarrage():

    # Cette fonction crée la fenêtre de démarrage du jeu.

    fenetre_demarrage = tk.Tk()
    fenetre_demarrage.title("Mot Mélè") 

    label_titre = tk.Label(fenetre_demarrage, text="Bienvenue au jeu Mot Mélès !")
    label_titre.pack(pady=10)

    # Par défaut, le jeu ne sera pas joué avec un timer
    # avec_timer = tk.BooleanVar()
    # avec_timer.set(False) 
    # bouton_demarrer_sans_timer = tk.Button(fenetre_demarrage, text="Démarrer le jeu sans timer", command=lambda: [fenetre_demarrage.destroy(), creer_menu(False)])
    # bouton_demarrer_sans_timer.pack(pady=5)
    # bouton_demarrer_avec_timer = tk.Button(fenetre_demarrage, text="Démarrer le jeu avec timer", command=lambda: [fenetre_demarrage.destroy(), creer_menu(True)])
    # bouton_demarrer_avec_timer.pack(pady=5)

    bouton_quitter = tk.Button(fenetre_demarrage, text="Quitter", command=fenetre_demarrage.quit)
    bouton_quitter.pack(pady=5)  

    fenetre_demarrage.mainloop()

# Charger les mots français depuis un fichier texte
def charger_mots_francais():
    # Cette fonction charge les mots français à partir d'un fichier texte.
    with open("words.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Générer un mot aléatoire à partir de la liste de mots français chargés
def generer_mot_aleatoire(mots_fr, taille_min, taille_max):
    # Cette fonction génère un mot aléatoire en fonction de la taille spécifiée.
    mots_filtres = [mot for mot in mots_fr if taille_min <= len(mot) <= taille_max]
    return random.choice(mots_filtres)

# Créer une fenêtre de démarrage avec des options pour commencer ou quitter
def creer_fenetre_demarrage():
    fenetre_windows = tk.Tk()
    fenetre_windows.title("Mot Mélès")

    label_titre = tk.Label(fenetre_windows, text="Bienvenue au jeu Mot Mélès !")
    label_titre.pack(pady=10)

    bouton_start = tk.Button(fenetre_windows, text="Start", command=lambda: [fenetre_windows.destroy(), creer_menu()])
    bouton_start.pack(pady=5)

    bouton_exit = tk.Button(fenetre_windows, text="Exit", command=fenetre_windows.quit)
    bouton_exit.pack(pady=5)

    fenetre_windows.mainloop()

# Générer une lettre majuscule aléatoire
def generer_lettre_aleatoire():
    # Cette fonction génère une lettre majuscule aléatoire.
    return random.choice(string.ascii_uppercase)

# Placer un mot dans la grille de jeu
def placer_mot_dans_grille(mot, grille):
    # Cette fonction place un mot dans la grille de jeu.
    lignes, colonnes = len(grille), len(grille[0])
    taille_mot = len(mot)
    if taille_mot > lignes and taille_mot > colonnes:
        raise ValueError("Le mot est trop grand pour la grille")

    direction = random.choice(['horizontal', 'vertical', 'diagonale'])
    if direction == 'horizontal':
        debut_ligne = random.randint(0, lignes - 1)
        debut_colonne = random.randint(0, colonnes - taille_mot)
    elif direction == 'vertical':
        debut_ligne = random.randint(0, lignes - taille_mot)
        debut_colonne = random.randint(0, colonnes - 1)
    else:
        debut_ligne = random.randint(0, lignes - taille_mot)
        debut_colonne = random.randint(0, colonnes - taille_mot)

    for i in range(taille_mot):
        if direction == 'horizontal':
            grille[debut_ligne][debut_colonne + i].config(text=mot[i])
        elif direction == 'vertical':
            grille[debut_ligne + i][debut_colonne].config(text=mot[i])
        else:
            grille[debut_ligne + i][debut_colonne + i].config(text=mot[i])

# Créer la grille de jeu
def creer_grille(fenetre, lignes, colonnes):
    # Cette fonction crée la grille de jeu.
    grille = [[None] * colonnes for _ in range(lignes)]
    for i in range(lignes):
        for j in range(colonnes):
            lettre = generer_lettre_aleatoire()
            cellule = tk.Label(fenetre, text=lettre, borderwidth=1, relief="solid", width=2, height=1)
            cellule.grid(row=i, column=j)
            grille[i][j] = cellule
            cellule.bind("<Button-1>", lambda event, row=i, column=j: commencer_trace(event, grille, row, column))
    return grille

# Créer la liste de mots sur le côté droit de la grille
def creer_liste_mots(fenetre, mots, lignes):
    # Cette fonction crée la liste des mots à droite de la grille.
    labels_mots = []
    for i, mot in enumerate(mots):
        label_mot = tk.Label(fenetre, text=mot.upper())
        label_mot.grid(row=i, column=lignes, sticky="w")  # Placer complètement à droite
        labels_mots.append(label_mot)
    return labels_mots

# Afficher "Mot trouvé" en dessous de la grille
def afficher_mot_trouve(fenetre):
    # Cette fonction affiche "Mot trouvé" en dessous de la grille.
    label_mot_trouve = tk.Label(fenetre, text="Mot trouvé", fg="green")
    label_mot_trouve.grid(row=11, column=0, columnspan=10)
    fenetre.after(1000, lambda: label_mot_trouve.config(text=""))

# Vérifier si tous les mots ont été trouvés
def verifier_mots_trouves(mots_trouves, labels_mots):
    # Cette fonction vérifie si tous les mots ont été trouvés.
    mots_restants = [mot.lower() for mot in labels_mots if mot.cget("text").lower() not in mots_trouves]
    return len(mots_restants) == 0

# Démarrer le tracé lorsqu'un clic est effectué sur une cellule de la grille
def commencer_trace(event, grille, row, column):
    # Cette fonction démarre le tracé lorsqu'un clic est effectué sur une cellule de la grille.
    global trace_active
    trace_active = True
    grille[row][column].config(bg="pink")
    grille[row][column].bind("<B1-Motion>", lambda event, r=row, c=column: tracer(event, grille, r, c))

# Continuer le tracé lorsqu'un mouvement de souris est détecté
def tracer(event, grille, row, column):
    # Cette fonction continue le tracé lorsqu'un mouvement de souris est détecté.
    global mots_trouves
    if trace_active:
        mot = grille[row][column].cget("text").lower()
        if mot in mots_trouves:
            grille[row][column].config(bg="blue")
            mots_trouves.append(mot)
            afficher_mot_trouve(grille[0][0].master)
            if verifier_mots_trouves(mots_trouves, labels_mots):
                afficher_message_victoire(grille[0][0].master)
        else:
            effacer_surlignement(grille)
    else:
        effacer_surlignement(grille)

# Effacer le surlignement de la grille
def effacer_surlignement(grille):
    # Cette fonction efface le surlignement de la grille.
    for ligne in grille:
        for cellule in ligne:
            cellule.config(bg="white")

# Fonction pour revenir au menu principal depuis le jeu
def retour_menu(fenetre_jeu):
    # Cette fonction permet de revenir au menu principal depuis le jeu.
    fenetre_jeu.destroy() 
    fenetre_menu.deiconify()  

# Créer l'interface du jeu en fonction du niveau de difficulté choisi
def creer_interface(difficulte):
    # Cette fonction crée l'interface du jeu en fonction du niveau de difficulté choisi.
    global fenetre_menu, fenetre_jeu, difficulte_actuelle, mots_trouves, labels_mots, grille
    fenetre_menu.withdraw() 
    difficulte_actuelle = difficulte

    mots_fr = charger_mots_francais()

    if difficulte == "Medium":
        lignes, colonnes = 7, 15
        mots = [generer_mot_aleatoire(mots_fr, 4, 6) for _ in range(10)]  
    elif difficulte == "Hard":
        lignes, colonnes = 15, 30
        mots = [generer_mot_aleatoire(mots_fr, 6, 9) for _ in range(10)]  
    else:
        lignes, colonnes = 5, 10
        mots = [generer_mot_aleatoire(mots_fr, 1, 3) for _ in range(10)]  

    fenetre_jeu = tk.Toplevel(fenetre_menu)  
    fenetre_jeu.title(f"Mot Mélangé - Level {difficulte}")

    frame_jeu = tk.Frame(fenetre_jeu)
    frame_jeu.pack(fill=tk.BOTH, expand=True)

    grille = creer_grille(frame_jeu, lignes, colonnes)
    labels_mots = creer_liste_mots(frame_jeu, mots, colonnes)
    mots_trouves = []

    for mot in mots:
        placer_mot_dans_grille(mot.upper(), grille)

    barre_menu = tk.Menu(fenetre_jeu)
    fenetre_jeu.config(menu=barre_menu)

    barre_menu.add_command(label="← Menu", command=lambda: retour_menu(fenetre_jeu))

# Créer le menu principal pour sélectionner le niveau de difficulté
def creer_menu():
    # Cette fonction crée le menu principal pour sélectionner le niveau de difficulté.
    global fenetre_menu
    fenetre_menu = tk.Tk()
    fenetre_menu.title("Menu de sélection de la difficulté")

    label_titre = tk.Label(fenetre_menu, text="Sélectionnez la difficulté")
    label_titre.pack(pady=10)

    def callback(difficulte):
        return lambda: creer_interface(difficulte)

    bouton_facile = tk.Button(fenetre_menu, text="Easy", command=callback("Easy"))
    bouton_facile.pack(pady=5)

    bouton_moyen = tk.Button(fenetre_menu, text="Medium", command=callback("Medium"))
    bouton_moyen.pack(pady=5)

    bouton_difficile = tk.Button(fenetre_menu, text="Hard", command=callback("Hard"))
    bouton_difficile.pack(pady=5)

    fenetre_menu.mainloop()

# Variable globale pour suivre l'état du tracé sur la grille
trace_active = False

# Lancer l'application en créant la fenêtre de démarrage
creer_fenetre_demarrage()