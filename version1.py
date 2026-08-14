#TIC TAC TOE USING PYTHON

import random

grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


empty = []

for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == " ":
            empty.append((row, col))

def computer_move():
    if empty:
        row, col = random.choice(empty)
        grid[row][col] = "O"
        empty.remove((row, col))

def player_move():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if grid[row][col] == " ":
                grid[row][col] = "X"
                empty.remove((row, col))
                break
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

def display_grid():
    print("╔═══╦═══╦═══╗")

    for i, row in enumerate(grid):
        print("║ " + " ║ ".join(row) + " ║")

        if i < len(grid) - 1:
            print("╠═══╬═══╬═══╣")

    print("╚═══╩═══╩═══╝")

def check_winner():
    j
    


while True:
    display_grid()
    player_move()

    # later: check winner

    display_grid()
    computer_move()

    # later: check winner