# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
age = int(input("How old are you? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("This is an odd number.")