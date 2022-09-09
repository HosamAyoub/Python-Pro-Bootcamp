number = int(input("Which number do you want to check?"))
#The bug here is because of the assign operator it should be == not assign operator =
#if number % 2 = 0:
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
