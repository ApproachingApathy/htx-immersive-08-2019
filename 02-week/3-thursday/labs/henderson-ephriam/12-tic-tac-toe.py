import time
import os

def clr_screen():
    os.system("cls||clear")

def banner(size, str_one, str_two):
    str_one_length = len(str_one)
    str_two_length = len(str_two)

    
    print("=" * size)
    print("=" * ((size - str_one_length)/2))
    print("=" * ((size - str_two_length)/2))

def drw_win_src(winner):
    clr_screen()
    print("=====================================")
    print("==========Congratulations!===========")
    print(f"==============={winner} Wins================")
    time.sleep(5)
    exit(0)

def win_checker(board):
    for line in board:
        #Check for horizontal wins.
        if line[0] == line[1] == line[2]  and line[0]!= " ":
            #print("Winner Detected")
            drw_win_src(line[0])
    #Iterates three times to check for vertical wins.
    for value in range(3):
        #print(value) #DEBUG
        if board[0][value] == board[1][value] == board[2][value] and board[1][value] != " ":
            #print("Winner Detected")
            drw_win_src(board[0][value])
    if board[0][0] == board[1][1] == board[2][2] and board[1][value] != " ":
        #print("Winner Detected")
        drw_win_src(board[0][0])   
    if board[2][0] == board[1][1] == board[0][2] and board[1][value] != " ":
        #print("Winner Detected")
        drw_win_src(board[2][0])
    
    is_draw = True
    for line in board:
        for position in line:
            if position == " ":
                is_draw = False
    if is_draw == True:
        clr_screen()
        print("It's a Draw!")
        time.sleep(5)
        exit(0)
    

       

def turn_changer(player):
    global turn
    if player == "X":
        turn = "O"
    else:
        turn =  "X"

def clr_board():
    board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

    return board
def drw_intro():
    os.system("cls||clear")
    print("=====================================")
    print("=======Let's Play Tic-Tac-Toe!=======")
    print("=====================================")
    time.sleep(3.5)
    #os.system("cls||clear")

def drw_board(board):
    
    print("  | 1 | 2 | 3 |")
    print("---------------")
    print(f"1 | {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("---------------")
    print(f"2 | {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("---------------")
    print(f"3 | {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("---------------")

def move(board, location, player):
    #TODO
    if board[location[0]][location[1]] == " ":
        board[location[0]][location[1]] = player
        turn_changer(player)
        return board
    else:
        print("That position is already filled! Try Again.")
        input("Press enter to continue...")
        return board




def get_move():
    successful_run = False
    while successful_run == False:
        raw_move = input("Which cell would you like to move to? Input your response as 'row,column' ")
        if raw_move.lower() == "quit":
            exit(0)
        positions = raw_move.split(",")
        for index, number in enumerate(positions):
            try:
                positions[index] = int(number)
                positions[index] -= 1
                print(positions[index])
                if positions[index] < 0 or positions[index] > 2:
                    print("Your selection is out of range!")
                    successful_run = False
                    break
                else:
                    successful_run = True
            except ValueError:
                print("I couldn't understand your intentions. Try again.")
                time.sleep(1.5)
                successful_run = False
                break
    return positions

board = clr_board()
turn = "X"
drw_intro()
player_dict = {"X": input("Who's playing X? "), "O": input("Who's playing O? ")}


while True:
    win_checker(board)
    print(f"It's {player_dict[turn]}'s turn.'")
    drw_board(board)
    location = get_move()

    #print("DEBUG")
    #print(location)
    board = move(board, location, turn)


    clr_screen()