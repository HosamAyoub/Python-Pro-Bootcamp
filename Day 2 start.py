#Data Types

#String
# print("Hello"[4])
# print("123" + "345")

#Integer
# print(123_456_789)
# print(123 + 345)

#Float
# 3.14

#Boolean
# True
# False

#Type Error, Type Checking and Type Conversion

# num_char = len(input("What is your name? "))
# print("Your name has "+ num_char + " characters")
# print(type(num_char))

num_char = len(input("What is your name? "))
print("Your name has "+ str(num_char) + " characters")
print(type(num_char))
#type casting
print(type(str(num_char)))