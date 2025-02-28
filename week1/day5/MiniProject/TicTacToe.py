square = {1 : 'none', 2 : 'none', 3 : 'none',
          4 : 'none', 5 : 'none', 6 : 'none',
          7 : 'none', 8 : 'none',9 : 'none'
        }

def display_board():
    print("\nTIC TAC TOE")
    print("********************")
    
    for i in square:
        if i in (1, 4, 7):
            print("* ", end=" ") 
        if square[i]== 'none':
            print(" ", end=" ") # " "
        else:
            print(square[i], end=" ") # X or O

        if i % 3 != 0:
            print("|", end=" ")
        else: 
            print("  *") # end of line
            if i < 7: 
                print("* ---|---|---  *")
    print("********************\n")
   

def player_input(player):  
    while 'none' in square.values(): 
        display_board()
        print(f"Player {player}'s turn...") 
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))
        
        # Convert row & column into board position (1-9)
        position = (row-1) * 3 + col

        # Check if the selected position is valid
        if position in square and square[position] == 'none':
            square[position] = player
            if check_win(player):
                display_board()
                print(f"Player {player} wins!")
                return # Exit game loop
            player = 'O' if player == 'X' else 'X'
        else: 
            print("Invalid position! Try again.")
    
    display_board()
    print("No winner. The game ends in a tie.")

def check_win(player):
    win_conditions = [
        [1,2,3], [4,5,6], [7,8,9], # rows
        [1,4,7], [2,5,8], [3,6,9], # columns
        [1,5,9], [3,5,7] # diagonals
    ]
    for condition in win_conditions:
        if all(square[pos] == player for pos in condition):
            return True
    return False

def play():
    print("Welcome to TIC TAC TOE!")
    player_input('X')

play()
