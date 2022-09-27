from random import randint

def display_board(board):
    print(board)


def enter_move(board):
    '''Make the user enter his move and return none'''
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
    '''Check if there us a free spots or not return True if there is free spots'''
    free_squares = []
    for free in range(1, 10):
        if str(free) in board:  
            free_squares.append(free)
    return len(free_squares) != 0


def victory_for(board, sign):
    '''Check the victory for the passed sign ('X' or 'O') and return True if there is a winner'''
    winning_cases = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
    arr = []
    pos = 0
    for i in range(board.count(sign)):
            sub = 0
            pos = board.index(sign, pos+1)
            if pos < 80:
                while pos - sub - 56 > 3:
                    sub += 7
                arr.append(pos - sub - 56)
            elif pos < 180:
                while pos - sub - 157 > 6:
                    sub += 7
                arr.append(pos - sub - 157)
            elif pos < 300:
                while pos - sub - 258 > 9:
                    sub += 7
                arr.append(pos - sub - 258)
    if len(arr) == 3:
        if arr in winning_cases:
            return True
    elif len(arr) == 4:
        for i in arr:
            temp = arr.copy()
            temp.remove(i)
            if temp in winning_cases:
                return True
    elif len(arr) == 5:
        for i in arr:
            temp = arr.copy()
            temp.remove(i)
            temp2 = temp.copy()
            for k in temp:
                temp2 = temp.copy()
                temp2.remove(k)
                if temp2 in winning_cases:
                    return True
    return False



#The start of the code I assumed that the computer will start at first and play at position 5   
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
            print("You win😎 ")
            break 
       
    while str(computer_move) not in board:
        computer_move = randint(1, 9)
        
    board = board.replace(str(computer_move), "X")
    display_board(board)
    if board.count('X') > 2:
        winner = victory_for(board, 'X')
        if winner:
            print("You lose🥱 ")
            break
else:
    print("It's a draw😶 ")