#TIC TAC TOE USING PYTHON

import random

grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


empty = []
player_moves = []
computer_moves = []

for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == " ":
            empty.append((row, col))

winning_combinations = [
                         [(0, 0), (0, 1), (0, 2)], # row 0
                         [(1, 0), (1, 1), (1, 2)], # row 1
                         [(2, 0), (2, 1), (2, 2)], # row 2
                         [(0, 0), (1, 0), (2, 0)], # column 0
                         [(0, 1), (1, 1), (2, 1)], # column 1
                         [(0, 2), (1, 2), (2, 2)], # column 2
                         [(0, 0), (1, 1), (2, 2)], # diagonal
                         [(0, 2), (1, 1), (2, 0)]  # other diagonal
                       ]

def computer_move():
    if empty:
        row, col = get_best_move()
        grid[row][col] = computer_symbol
        empty.remove((row, col))
        computer_moves.append((row, col))


def player_move():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if grid[row][col] == " ":
                grid[row][col] = player_symbol
                empty.remove((row, col))
                player_moves.append((row, col))
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def get_best_move():
    
       #Decides whether computer is winning or not
    for combination in winning_combinations:
        count = 0
        for move in computer_moves:
            if move in combination:
                count += 1

        if count == 2:
            for coordinate in combination:
                if coordinate in empty:
                    return coordinate
         #Decides whether player needs to be blocked or not     
    for combination in winning_combinations:
        count = 0
        for move in player_moves:
            if move in combination:
                count += 1
        if count == 2:
            for coordinate in combination:
                if coordinate in empty:
                    return coordinate

    return random.choice(empty)

def display_grid():
    print("╔═══╦═══╦═══╗")

    for i, row in enumerate(grid):
        print("║ " + " ║ ".join(row) + " ║")

        if i < len(grid) - 1:
            print("╠═══╬═══╬═══╣")

    print("╚═══╩═══╩═══╝")

def check_winner(symbol):
    for combination in winning_combinations:
        if all(grid[row][col] == symbol for row, col in combination):
            return True
    return False
    
    
def check_game_over():
    if check_winner(player_symbol):
        print("Congratulations! You won!")
        return True
    elif check_winner(computer_symbol):
        print("Computer wins!")
        
        return True
    elif not empty:
        print("It's a draw!")
        
        return True
    return False

while True:
    print("Welcome to TIC TAC TOE!")
    key = input("Choose your symbol (X or O): ").upper()
    if key not in ["X", "O"]:
        print("Invalid input. Please choose either X or O.")
        continue
    if key == "X":
        player_symbol = "X"
        computer_symbol = "O"
    else:
        player_symbol = "O"
        computer_symbol = "X"


    if player_symbol == "X":
        display_grid()
        player_move()
        
        if check_game_over():
            display_grid()
            break
        
        display_grid()
        computer_move()
        
        if check_game_over():
            display_grid()
            break

    else:
        display_grid()
        computer_move()
        
        if check_game_over():
            display_grid()
            break
        
        display_grid()
        player_move()
        
        if check_game_over():
            display_grid()
            break
           
    