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

# Load French words from a text file
def load_french_words():
    with open("words.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Generate a random word from the loaded French words list
def generate_random_word(french_words, min_length, max_length):
    filtered_words = [word for word in french_words if min_length <= len(word) <= max_length]
    return random.choice(filtered_words)

# Function to create the game start window
def create_start_window():
    start_window = tk.Tk()
    start_window.title("Word Scrambler") 

    title_label = tk.Label(start_window, text="Welcome to the Word Scrambler game!")
    title_label.pack(pady=10)

    start_button = tk.Button(start_window, text="Start the game", command=lambda: [start_window.destroy(), create_menu()])
    start_button.pack(pady=5)

    quit_button = tk.Button(start_window, text="Quit", command=start_window.quit)
    quit_button.pack(pady=5)  

    start_window.mainloop()

# Global variable to store the current letter arrangement
letter_arrangement = []

# Function to store the current letter arrangement
def store_letter_arrangement(grid):
    global letter_arrangement
    letter_arrangement = [[cell.cget("text") for cell in row] for row in grid]

# Function to reload the grid with the current letter arrangement
def reload_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].config(text=letter_arrangement[i][j])

# Create a new grid with words based on another theme
def change_theme():
    global word_labels, found_words
    french_words = load_french_words()
    new_words = [generate_random_word(french_words, len(word), len(word)) for word in word_labels]
    for i, word in enumerate(new_words):
        word_labels[i].config(text=word.upper())
    found_words = []
    reload_grid(grid)

# Generate a random uppercase letter
def generate_random_letter():
    return random.choice(string.ascii_uppercase)

# Place a word in the game grid
def place_word_in_grid(word, grid):
    rows, columns = len(grid), len(grid[0])
    word_length = len(word)
    if word_length > rows and word_length > columns:
        raise ValueError("The word is too big for the grid")

    direction = random.choice(['horizontal', 'vertical', 'diagonal'])
    if direction == 'horizontal':
        start_row = random.randint(0, rows - 1)
        start_column = random.randint(0, columns - word_length)
    elif direction == 'vertical':
        start_row = random.randint(0, rows - word_length)
        start_column = random.randint(0, columns - 1)
    else:
        start_row = random.randint(0, rows - word_length)
        start_column = random.randint(0, columns - word_length)

    for i in range(word_length):
        if direction == 'horizontal':
            grid[start_row][start_column + i].config(text=word[i])
        elif direction == 'vertical':
            grid[start_row + i][start_column].config(text=word[i])
        else:
            grid[start_row + i][start_column + i].config(text=word[i])

# Create the game grid
def create_grid(window, rows, columns):
    grid = [[None] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            letter = generate_random_letter()
            cell = tk.Label(window, text=letter, borderwidth=1, relief="solid", width=2, height=1)
            cell.grid(row=i, column=j)
            grid[i][j] = cell
    return grid

# Create the list of words on the right side of the grid
def create_word_list(window, words, rows):
    word_labels = []
    for i, word in enumerate(words):
        word_label = tk.Label(window, text=word.upper())
        word_label.grid(row=i, column=rows, sticky="w")  # Place completely to the right
        word_labels.append(word_label)
    return word_labels

# Display "Word found" below the grid
def display_word_found(window):
    word_found_label = tk.Label(window, text="Word found", fg="green")
    word_found_label.grid(row=11, column=0, columnspan=10)
    window.after(1000, lambda: word_found_label.config(text=""))

# Check if all words have been found
def check_words_found(found_words, word_labels):
    remaining_words = [word.lower() for word in word_labels if word.cget("text").lower() not in found_words]
    return len(remaining_words) == 0

# Start tracing when a click is made on a grid cell
def start_tracing(event, grid, row, column):
    global tracing_active
    tracing_active = True
    grid[row][column].config(bg="pink")
    grid[row][column].bind("<B1-Motion>", lambda event, r=row, c=column: continue_tracing(event, grid, r, c))

# Continue tracing when mouse movement is detected
def continue_tracing(event, grid, row, column):
    global found_words
    if tracing_active:
        word = grid[row][column].cget("text").lower()
        if word in found_words:
            grid[row][column].config(bg="blue")
            found_words.append(word)
            display_word_found(grid[0][0].master)
            if check_words_found(found_words, word_labels):
                display_victory_message(grid[0][0].master)
        else:
            clear_highlighting(grid)
    else:
        clear_highlighting(grid)

# Clear grid highlighting
def clear_highlighting(grid):
    for row in grid:
        for cell in row:
            cell.config(bg="white")

# Function to return to the main menu from the game
def return_to_menu(game_window, main_menu_window):
    game_window.destroy() 
    main_menu_window.deiconify()

# Create the game interface based on the selected difficulty level
def create_interface(difficulty, main_menu_window):
    global game_window, current_difficulty, found_words, word_labels, grid
    main_menu_window.withdraw() 
    current_difficulty = difficulty

    french_words = load_french_words()

    if difficulty == "Medium":
        rows, columns = 7, 15
        words = [generate_random_word(french_words, 4, 6) for _ in range(10)]  
    elif difficulty == "Hard":
        rows, columns = 15, 30
        words = [generate_random_word(french_words, 6, 9) for _ in range(10)]  
    else:
        rows, columns = 5, 10
        words = [generate_random_word(french_words, 1, 3) for _ in range(10)]  

    game_window = tk.Toplevel(main_menu_window)  
    game_window.title(f"Word Scrambler - Level {difficulty}")

    game_frame = tk.Frame(game_window)
    game_frame.pack(fill=tk.BOTH, expand=True)

    grid = create_grid(game_frame, rows, columns)
    word_labels = create_word_list(game_frame, words, columns)
    found_words = []

    store_letter_arrangement(grid)

    for word in words:
        place_word_in_grid(word.upper(), grid)

    menu_bar = tk.Menu(game_window)
    game_window.config(menu=menu_bar)

    menu_bar.add_command(label="← Menu", command=lambda: return_to_menu(game_window, main_menu_window))

# Create the main menu to select the difficulty level
def create_menu():
    main_menu_window = tk.Tk()
    main_menu_window.title("Main Menu")

    label = tk.Label(main_menu_window, text="Select difficulty :")
    label.pack(pady=10)

    buttons_frame = tk.Frame(main_menu_window)
    buttons_frame.pack(pady=5)

    easy_button = tk.Button(buttons_frame, text="Easy", command=lambda: create_interface("Easy", main_menu_window))
    easy_button.grid(row=0, column=0, padx=5)

    medium_button = tk.Button(buttons_frame, text="Medium", command=lambda: create_interface("Medium", main_menu_window))
    medium_button.grid(row=0, column=1, padx=5)

    hard_button = tk.Button(buttons_frame, text="Hard", command=lambda: create_interface("Hard", main_menu_window))
    hard_button.grid(row=0, column=2, padx=5)

    exit_button = tk.Button(main_menu_window, text="Exit", command=main_menu_window.destroy)
    exit_button.pack(pady=5)

    main_menu_window.mainloop()

# Create the game start window
create_start_window()