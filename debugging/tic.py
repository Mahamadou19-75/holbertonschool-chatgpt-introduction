#!/usr/bin/python3
def print_board(board):
    """Affiche le plateau"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie toutes les conditions de victoire"""

    # Vérification des lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]

    # Vérification des colonnes
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Vérification des diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None  # Pas de gagnant

def get_valid_input(prompt):
    """Force l'utilisateur à entrer une valeur correcte : 0, 1 ou 2"""
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Veuillez entrer 0, 1 ou 2.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0  # compteur pour détecter un match nul

    while True:
        print_board(board)

        print(f"Tour du joueur {player}")

        row = get_valid_input("Entrez la ligne (0, 1, 2) : ")
        col = get_valid_input("Entrez la colonne (0, 1, 2) : ")

        if board[row][col] != " ":
            print("Cette case est déjà prise, réessayez.")
            continue

        board[row][col] = player
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Le joueur {winner} a gagné !")
            break

        if moves == 9:
            print_board(board)
            print("Match nul !")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
