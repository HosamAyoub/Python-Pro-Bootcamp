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
    winning_cases = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    arr = []
    pos = 0
    if sign == 'X':
        for i in range(board.count("X")):
            sub = 0
            pos = board.index("X", pos+1)
            if pos < 80:
                while pos - sub - 56 > 3:
                    sub += 7
                X.append(pos - sub - 56)
            elif pos < 180:
                while pos - sub - 157 > 6:
                    sub += 7
                X.append(pos - sub - 157)
            elif pos < 300:
                while pos - sub - 258 > 9:
                    sub += 7
                X.append(pos - sub - 258)
        if X in winning_cases:
            print("You lose🥱 ")
            return True
    elif sign == 'O':
        for i in range(board.count("O")):
            sub = 0
            pos = board.index("O", pos+1)
            if pos < 80:
                while pos - sub - 56 > 3:
                    sub += 7
                O.append(pos - sub - 56)
            elif pos < 180:
                while pos - sub - 157 > 6:
                    sub += 7
                O.append(pos - sub - 157)
            elif pos < 300:
                while pos - sub - 258 > 9:
                    sub += 7
                O.append(pos - sub - 258)
        if O in winning_cases:
            print("You win😎 ")
            return True
    return False


board = '''
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
'''
winner = 0
display_board(board)
computer_move = 5

while (make_list_of_free_fields(board)):
    board = enter_move(board)
    if board.count('O') > 2:
        winner = victory_for(board, 'O')
        if winner:
            break 
       
    while str(computer_move) not in board:
        computer_move = randint(1, 9)
        
    board = board.replace(str(computer_move), "X")
    display_board(board)
    if board.count('X') > 2:
        winner = victory_for(board, 'X')
        if winner:
            break
else:
    print("It's a draw😶 ")