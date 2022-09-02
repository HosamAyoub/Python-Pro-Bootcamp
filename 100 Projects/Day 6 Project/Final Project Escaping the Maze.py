def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

count = 0
while not at_goal():
    if not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
        count += 1
        if (count == 4):
            turn_left()  
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
