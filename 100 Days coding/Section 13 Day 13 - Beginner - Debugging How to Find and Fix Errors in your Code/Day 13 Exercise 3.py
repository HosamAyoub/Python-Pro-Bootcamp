for number in range(1, 101):
#the first logic error her is because of (or) it should be (and) cause we need to print "FizzBuzz" only when the number is divisble by both 3 and 5 no just one of them
  # if number % 3 == 0 or number % 5 == 0:
  #   print("FizzBuzz")
#Second logic error here that just need to print "FizzBuzz" if the number was divisible by 3 and 5 not print "FizzBuzz" "Fizz" "Buzz" so we just need one if and others will be elif
  # if number % 3 == 0:
  #   print("Fizz")
  # if number % 5 == 0:
  #   print("Buzz")
  # else:
#We need to print the number it self no list of the number
  #   print([number])

  #Solution
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print(number)