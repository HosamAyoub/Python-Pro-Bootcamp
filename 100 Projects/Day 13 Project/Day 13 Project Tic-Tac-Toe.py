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
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.

displ