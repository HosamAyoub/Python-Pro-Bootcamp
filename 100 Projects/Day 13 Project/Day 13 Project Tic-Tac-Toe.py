def display_board(board):
    print(board)


def enter_move(board):
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if str(user_move) in board:
                board = board.replace(str(user_move), "O")
                display_board(board)
                return board
            else:
                print("Please enter a valid the spot number")
        except:
            print("Please enter a number.")


def make_list_of_free_fields(board):
    free_squares = []
    for free in range(1, 10):
        if str(free) in board:  
            free_squares.append(free)
    return len(free_squares) != 0


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.

displ