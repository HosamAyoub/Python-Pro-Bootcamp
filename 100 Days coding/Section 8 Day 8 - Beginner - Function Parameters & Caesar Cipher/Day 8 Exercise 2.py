def prime_checker(number):
    for iterater in range (2, number):
        if (number % iterater == 0):
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)