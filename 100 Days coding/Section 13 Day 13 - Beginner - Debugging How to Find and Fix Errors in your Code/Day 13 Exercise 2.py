#The bug will be generated from the year variable because we forgot to typecast it to int so that it can work fine with numerical operations
# year = input("Which year do you want to check?")
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")