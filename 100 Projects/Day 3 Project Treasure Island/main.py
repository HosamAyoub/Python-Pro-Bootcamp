print('''
*************************************
    _                ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
       
*************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
order = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n")

if (order == "right") or (order == "Right") or (order == "RIGHT") or (order == "rIGHT"):
  order = input("You come to a lake. There is an islan in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n")
  if (order == "wait") or (order == "Wait") or (order == "WAIT") or (order == "wAIT"):
    order = input("You arrive at the island. There is house with 3 doors. One red, One yellow, and One blue. Which color do you choose? \n")
    if (order == "blue") or (order == "Blue") or (order == "BLUE") or (order == "bLUE"):
      print("You found the treasure! You Win!")
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
    elif (order == "red") or (order == "Red") or (order == "RED") or (order == "rED"):
      print("It's a room full of fire. Game Over.")
    elif (order == "yellow") or (order == "Yellow") or (order == "YELLOW") or (order == "yELLOW"):
      print("You get eaten by beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game over")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")