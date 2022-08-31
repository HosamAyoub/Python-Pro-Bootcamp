# import random
# #random integer number from 1 to 10
# random_integer = random.randint(1, 10)
# print(random_integer)
# #random float number from 0.00000000000 to 0.99999999999999...
# random_float = random.random()
# print(random_float)
# ##random float number from 0.00000000000 to 9.99999999999999...
# random_big_float = random.random() + random.randint(1, 10)
# print(random_big_float)

import random
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
mylist.append("Strawberry")
print(mylist)
mylist.extend(["Mango", "Peach"])
print(mylist)
print(len(mylist))
print(random.choice(mylist))
print(random.choice(mylist))
print(random.choice(mylist))

str_input = input("Enter any word: \n")
str_arr = str_input.split(" ")
print(str_arr)
print(len(str_arr))