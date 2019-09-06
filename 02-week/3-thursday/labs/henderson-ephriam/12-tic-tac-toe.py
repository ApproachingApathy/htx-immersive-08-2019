import time
import os

def clr_screen():
    os.system("cls||clear")

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
    if board[0][location[0]][location[1]] == " ":
        board[location[0]][location[1]] = player
        turn_changer(player)
        return [board, True]
    else:
        print("That position is already filled!")
        return [board[0], False]




def get_move():
    successful_run = False
    while successful_run == False:
        raw_move = input("Which cell would you like to move to? Input your response as 'row,column' ")
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
                break
    return positions

board = [clr_board(), False]
turn = "X"
drw_intro()

while True:
    print(f"It's {turn}'s turn.'")
    drw_board(board[0])
    location = get_move()
    turn_success = False
    while turn_success == False:
        print("DEBUG")
        print(location)
        board = move(board, location, turn)
        if board != 0 :
            turn_success = True
        else:
            location = get_move()

    clr_screen()