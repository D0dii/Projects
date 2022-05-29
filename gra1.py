board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

def print_board():
    return f'*****\n{board[0]} {board[1]} {board[2]} \n{board[3]} {board[4]} {board[5]} \n{board[6]} {board[7]} {board[8]}\n*****'

def print_board_start():
    return f'Positions:\n1 2 3\n4 5 6 \n7 8 9 '

def choose_if_start():
    player = None
    computer = None
    decision = input("Do you want to start?: ")
    if decision == "yes":
        player = 1
        computer = 2
    elif decision == "no":
        computer = 1
        player = 2

    return player,computer
        

def player_move(board,player_sign):
    player_move = int(input("Which position do you choose?: ")) - 1
    while board[player_move] != "-":
        player_move = int(input("Which position do you choose?: ")) - 1

    board[player_move] = player_sign
    return board,player_sign

def check_if_win_lose_comp(board,computer_sign,player_sign):
    for a in range(len(board)-1):
        if board[a] == "-":
            board[a] = computer_sign
            winner = check_win(board)
            if computer_sign == winner:
                board[a] = "-"
                return a
            else:
                board[a] = "-"

    for b in range(len(board)-1):
        if board[b] == "-":
            board[b] = player_sign
            winner_b = check_win(board)
            if player_sign == winner_b:
                board[b] = "-"
                return b
            else:
                board[b] = "-" 



def computer_move(board,computer_sign,player_sign):
    move = check_if_win_lose_comp(board,computer_sign,player_sign)
    if move != None:
        board[move] = computer_sign
        return board,computer_sign,player_sign
    else:
        if board[4] == "-":
            board[4] = computer_sign
            return board,computer_sign,player_sign
        else:
            if board[0] == "-":
                board[0] = computer_sign
                return board,computer_sign,player_sign
            elif board[2] == "-":
                board[2] = computer_sign
                return board,computer_sign,player_sign
            elif board[6] == "-":
                board[6] = computer_sign
                return board,computer_sign,player_sign
            elif board[8] == "-":
                board[8] = computer_sign
                return board,computer_sign,player_sign
            else:
                for c in range(len(board)-1):
                    if board[c] == "-":
                        board[c] = computer_sign
                        return board,computer_sign,player_sign


def check_win(board):
    winner = None
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
    if board[0] == board[4] == board[8] != "-":
        winner = board[4]
    if board[2] == board[4] == board[6] != "-":
        winner = board[4]

    return winner


def game():
    turn = 1
    player,computer = choose_if_start()
    print(print_board_start())
    count = 0
    if player == 1:
            player_sign = "X"
            computer_sign = "O"
    else:
        player_sign = "O"
        computer_sign = "X"
    while True:
        print(print_board())
        if turn == player:
            player_move(board,player_sign)
        elif turn == computer:
            print("computer moves")
            computer_move(board,computer_sign,player_sign)                  
        winner = check_win(board)
        if computer_sign == winner:
            print("computer won!")
            print_board(board)
            break
        elif player_sign == winner:
            print("player won!")
            print_board(board)
            break
        if turn == 1:
            turn = 2
        else:
            turn = 1
        count += 1
        if count == 9:
            print("It's a tie!")
            print(print_board())
            break

game()