# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
concatenation = name1.lower() + name2.lower()
true = concatenation.count("t") + concatenation.count("r") + concatenation.count("u") + concatenation.count("e")
love = concatenation.count("l") + concatenation.count("o") + concatenation.count("v") + concatenation.count("e")
score = true * 10 + love
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")