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
import random
import string

# Charger les mots français depuis un fichier texte
def charger_mots_francais():
    with open("words.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Générer un mot aléatoire à partir de la liste de mots français chargés
def generer_mot_aleatoire(mots_fr, taille_min, taille_max):
    mots_filtres = [mot for mot in mots_fr if taille_min <= len(mot) <= taille_max]
    return random.choice(mots_filtres)

# Fonction pour créer la fenêtre de démarrage du jeu
def creer_fenetre_demarrage():
    fenetre_demarrage = tk.Tk()
    fenetre_demarrage.title("Mot Mélangé") 

    label_titre = tk.Label(fenetre_demarrage, text="Bienvenue au jeu Mot Mélangé !")
    label_titre.pack(pady=10)

    bouton_demarrer = tk.Button(fenetre_demarrage, text="Démarrer le jeu", command=lambda: [fenetre_demarrage.destroy(), creer_menu()])
    bouton_demarrer.pack(pady=5)

    bouton_quitter = tk.Button(fenetre_demarrage, text="Quitter", command=fenetre_demarrage.quit)
    bouton_quitter.pack(pady=5)  

    fenetre_demarrage.mainloop()

# Variable globale pour mémoriser la disposition actuelle de lettres
disposition_lettres = []

# Fonction pour mémoriser la disposition actuelle de lettres
def memoriser_disposition_lettres(grille):
    global disposition_lettres
    disposition_lettres = [[cellule.cget("text") for cellule in ligne] for ligne in grille]

# Fonction pour recharger la grille avec la disposition actuelle de lettres
def recharger_grille(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            grille[i][j].config(text=disposition_lettres[i][j])

# Créer une nouvelle grille avec des mots basés sur un autre thème
def changer_theme():
    global labels_mots, mots_trouves
    mots_fr = charger_mots_francais()
    nouveaux_mots = [generer_mot_aleatoire(mots_fr, len(mot), len(mot)) for mot in labels_mots]
    for i, mot in enumerate(nouveaux_mots):
        labels_mots[i].config(text=mot.upper())
    mots_trouves = []
    recharger_grille(grille)

# Générer une lettre majuscule aléatoire
def generer_lettre_aleatoire():
    return random.choice(string.ascii_uppercase)

# Placer un mot dans la grille de jeu
def placer_mot_dans_grille(mot, grille):
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
    grille = [[None] * colonnes for _ in range(lignes)]
    for i in range(lignes):
        for j in range(colonnes):
            lettre = generer_lettre_aleatoire()
            cellule = tk.Label(fenetre, text=lettre, borderwidth=1, relief="solid", width=2, height=1)
            cellule.grid(row=i, column=j)
            grille[i][j] = cellule
    return grille

# Créer la liste de mots sur le côté droit de la grille
def creer_liste_mots(fenetre, mots, lignes):
    labels_mots = []
    for i, mot in enumerate(mots):
        label_mot = tk.Label(fenetre, text=mot.upper())
        label_mot.grid(row=i, column=lignes, sticky="w")  # Placer complètement à droite
        labels_mots.append(label_mot)
    return labels_mots

# Afficher "Mot trouvé" en dessous de la grille
def afficher_mot_trouve(fenetre):
    label_mot_trouve = tk.Label(fenetre, text="Mot trouvé", fg="green")
    label_mot_trouve.grid(row=11, column=0, columnspan=10)
    fenetre.after(1000, lambda: label_mot_trouve.config(text=""))

# Vérifier si tous les mots ont été trouvés
def verifier_mots_trouves(mots_trouves, labels_mots):
    mots_restants = [mot.lower() for mot in labels_mots if mot.cget("text").lower() not in mots_trouves]
    return len(mots_restants) == 0

# Démarrer le tracé lorsqu'un clic est effectué sur une cellule de la grille
def demarrer_tracage(event, grille, ligne, colonne):
    global tracage_actif
    tracage_actif = True
    grille[ligne][colonne].config(bg="pink")
    grille[ligne][colonne].bind("<B1-Motion>", lambda event, l=ligne, c=colonne: continuer_tracage(event, grille, l, c))

# Continuer le tracé lorsqu'un mouvement de souris est détecté
def continuer_tracage(event, grille, ligne, colonne):
    global mots_trouves
    if tracage_actif:
        mot = grille[ligne][colonne].cget("text").lower()
        if mot in mots_trouves:
            grille[ligne][colonne].config(bg="blue")
            mots_trouves.append(mot)
            afficher_mot_trouve(grille[0][0].master)
            if verifier_mots_trouves(mots_trouves, labels_mots):
                afficher_message_victoire(grille[0][0].master)
        else:
            effacer_mise_en_surbrillance(grille)
    else:
        effacer_mise_en_surbrillance(grille)

# Effacer la mise en surbrillance de la grille
def effacer_mise_en_surbrillance(grille):
    for ligne in grille:
        for cellule in ligne:
            cellule.config(bg="white")

# Fonction pour revenir au menu principal depuis le jeu
def retourner_au_menu(fenetre_jeu, fenetre_menu):
    fenetre_jeu.destroy() 
    fenetre_menu.deiconify()

# Créer l'interface du jeu en fonction du niveau de difficulté choisi
def creer_interface(difficulte, fenetre_menu):
    global fenetre_jeu, difficulte_actuelle, mots_trouves, labels_mots, grille
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
    fenetre_jeu.title(f"Mot Mélangé - Niveau {difficulte}")

    frame_jeu = tk.Frame(fenetre_jeu)
    frame_jeu.pack(fill=tk.BOTH, expand=True)

    grille = creer_grille(frame_jeu, lignes, colonnes)
    labels_mots = creer_liste_mots(frame_jeu, mots, colonnes)
    mots_trouves = []

    memoriser_disposition_lettres(grille)

    for mot in mots:
        placer_mot_dans_grille(mot.upper(), grille)

    barre_menu = tk.Menu(fenetre_jeu)
    fenetre_jeu.config(menu=barre_menu)

    barre_menu.add_command(label="← Menu", command=lambda: retourner_au_menu(fenetre_jeu, fenetre_menu))

# Créer le menu principal pour sélectionner le niveau de difficulté
def creer_menu():
    fenetre_principale = tk.Tk()
    fenetre_principale.title("Menu Principal")

    label = tk.Label(fenetre_principale, text="Select difficulty :")
    label.pack(pady=10)

    buttons_frame = tk.Frame(fenetre_principale)
    buttons_frame.pack(pady=5)

    easy_button = tk.Button(buttons_frame, text="Easy", command=lambda: creer_interface("Easy", fenetre_principale))
    easy_button.grid(row=0, column=0, padx=5)

    medium_button = tk.Button(buttons_frame, text="Medium", command=lambda: creer_interface("Medium", fenetre_principale))
    medium_button.grid(row=0, column=1, padx=5)

    hard_button = tk.Button(buttons_frame, text="Hard", command=lambda: creer_interface("Hard", fenetre_principale))
    hard_button.grid(row=0, column=2, padx=5)

    exit_button = tk.Button(fenetre_principale, text="Exit", command=fenetre_principale.destroy)
    exit_button.pack(pady=5)

    fenetre_principale.mainloop()

# Créer la fenêtre de démarrage du jeu
creer_fenetre_demarrage()
