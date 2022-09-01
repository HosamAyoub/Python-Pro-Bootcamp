#Write your code below this row 👇
for iterator in range(1, 101):
  if (iterator % 3 == 0) and (iterator % 5 == 0):
    print("FizzBuzz")
  elif (iterator % 3 == 0):
    print("Fizz")
  elif (iterator % 5 == 0):
    print("Buzz")
  else:
    print(iterator)