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
    # This function loads French words from a text file.
    with open("words.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Generate a random word from the loaded French words list
def generate_random_word(french_words, min_length, max_length):
    # This function generates a random word based on the specified length.
    filtered_words = [word for word in french_words if min_length <= len(word) <= max_length]
    return random.choice(filtered_words)

# Function to create the game startup window
def create_startup_window():
    # This function creates the game startup window.
    startup_window = tk.Tk()
    startup_window.title("Word Mixup")
    
    # Add the welcome message as a Label widget
    welcome_label = tk.Label(startup_window, text="Welcome to the Word Mixup Game!")
    welcome_label.pack(pady=10)

    start_button = tk.Button(startup_window, text="Start!", command=lambda: [startup_window.destroy(), create_menu()])
    start_button.pack(pady=5)

    quit_button = tk.Button(startup_window, text="Quit", command=startup_window.quit)
    quit_button.pack(pady=5)

    startup_window.mainloop()

# Generate a random uppercase letter
def generate_random_letter():
    # This function generates a random uppercase letter.
    return random.choice(string.ascii_uppercase)

# Place a word in the game grid
def place_word_in_grid(word, grid):
    # This function places a word in the game grid.
    rows, columns = len(grid), len(grid[0])
    word_length = len(word)
    if word_length > rows and word_length > columns:
        raise ValueError("The word is too large for the grid")

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
    # This function creates the game grid.
    grid = [[None] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            letter = generate_random_letter()
            cell = tk.Label(window, text=letter, borderwidth=1, relief="solid", width=2, height=1)
            cell.grid(row=i, column=j)
            grid[i][j] = cell
            cell.bind("<Button-1>", lambda event, row=i, column=j: start_trace(event, grid, row, column))
    return grid

# Create the list of words on the right side of the grid
def create_word_list(window, words, columns):
    # This function creates the list of words on the right side of the grid.
    word_labels = []
    for i, word in enumerate(words):
        word_label = tk.Label(window, text=word.upper())
        word_label.grid(row=i, column=columns, sticky="w")  # Place completely to the right
        word_labels.append(word_label)
    return word_labels

# Display "Word found" below the grid
def display_word_found(window):
    # This function displays "Word found" below the grid.
    word_found_label = tk.Label(window, text="Word found", fg="green")
    word_found_label.grid(row=11, column=0, columnspan=10)
    window.after(1000, lambda: word_found_label.config(text=""))

# Check if all words have been found
def check_words_found(found_words, word_labels):
    # This function checks if all words have been found.
    remaining_words = [word.lower() for word in word_labels if word.cget("text").lower() not in found_words]
    return len(remaining_words) == 0

# Start tracing when a click is made on a cell in the grid
def start_trace(event, grid, row, column):
    # This function starts tracing when a click is made on a cell in the grid.
    global trace_active
    trace_active = True
    grid[row][column].config(bg="pink")
    grid[row][column].bind("<B1-Motion>", lambda event, r=row, c=column: trace(event, grid, r, c))

# Continue tracing when mouse movement is detected
def trace(event, grid, row, column):
    # This function continues tracing when mouse movement is detected.
    global found_words
    if trace_active:
        word = grid[row][column].cget("text").lower()
        if word in found_words:
            grid[row][column].config(bg="blue")
            found_words.append(word)
            display_word_found(grid[0][0].master)
            if check_words_found(found_words, word_labels):
                display_victory_message(grid[0][0].master)
        else:
            clear_highlight(grid)
    else:
        clear_highlight(grid)

# Clear the grid highlight
def clear_highlight(grid):
    # This function clears the grid highlight.
    for row in grid:
        for cell in row:
            cell.config(bg="white")

# Function to return to the main menu from the game
def return_to_menu(game_window):
    # This function allows returning to the main menu from the game.
    game_window.destroy() 
    menu_window.deiconify()  

# Create the main menu to select the difficulty level
def create_menu():
    # This function creates the main menu to select the difficulty level.
    global menu_window
    menu_window = tk.Tk()
    menu_window.title("Difficulty Selection Menu")

    title_label = tk.Label(menu_window, text="Select the difficulty")
    title_label.pack(pady=10)

    def callback(difficulty):
        return lambda: create_interface(difficulty)

    easy_button = tk.Button(menu_window, text="Easy", command=callback("Easy"))
    easy_button.pack(pady=5)

    medium_button = tk.Button(menu_window, text="Medium", command=callback("Medium"))
    medium_button.pack(pady=5)

    hard_button = tk.Button(menu_window, text="Hard", command=callback("Hard"))
    hard_button.pack(pady=5)
    
    # Button to exit the application
    exit_button = tk.Button(menu_window, text="Exit", command=menu_window.destroy)  # Close the menu window
    exit_button.pack(pady=5)

    menu_window.mainloop()

# Global variable to track the trace state on the grid
trace_active = False

# Launch the application by creating the startup window
create_startup_window()
