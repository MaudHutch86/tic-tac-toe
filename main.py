import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
GameRunning = True


# todo 1: printing the game board

def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])


# todo 2: take player input

def player_input(board):
    play_input = int(input("enter a number between 1 to 9:"))
    if 1 <= play_input <= 9 and board[play_input - 1] == "-":
        board[play_input - 1] = currentPlayer
    else:
        print("Too bad there is no space here")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
        print(f"the winner is {winner}")
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
        print(f"the winner is {winner}")
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True
        print(f"the winner is {winner}")


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
        print(f"the winner is {winner}")
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
        print(f"the winner is {winner}")
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True
        print(f"the winner is {winner}")


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
        print(f"the winner is {winner}")
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
        print(f"the winner is {winner}")


# todo 4: switch the player
def switch_player():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def ai_player(board):
    while currentPlayer == "O":
        ai_play = random.randint(0, 8)
        if board[ai_play] == "-":
            board[ai_play] = "O"
            switch_player()


# todo 5: for win or tie again


# todo 3 : check for win or tie
def check_tie(board):
    global GameRunning
    if "-" not in board:
        print_board(board)
        print("It is a tie")
        GameRunning = False


# todo 6: check for win or tie
def check_win():
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        print(f"the winner is {winner}")


while GameRunning:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    ai_player(board)
    check_tie(board)








