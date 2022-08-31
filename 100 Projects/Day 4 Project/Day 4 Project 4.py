import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = [rock, paper , scissors]
computer_choice = random.randint(0, 2)

enemy = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if enemy > 3 or enemy < 0:
  print("You types invalid input, you lose!")
elif enemy == computer_choice:
  print("Your chose:\n" + game[enemy])
  print("Computer chose:\n" + game[computer_choice])
  print("It's a draw!")
else:
  if ((enemy == 0) and (computer_choice == 2)) or ((enemy == 1) and (computer_choice == 0) or ((enemy == 2) and (computer_choice == 1))):
    print("Your chose:\n" + game[enemy])
    print("Computer chose:\n" + game[computer_choice])
    print("You win!")
  else:
    print("Your chose:\n" + game[enemy])
    print("Computer chose:\n" + game[computer_choice])
    print("You lose!")