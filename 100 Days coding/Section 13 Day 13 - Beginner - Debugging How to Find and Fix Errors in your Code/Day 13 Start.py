############DEBUGGING#####################

# # Describe Problem
#The for loop count from 1 to 19, the function will print "You got it" when the value of i become 20 and that will never happen so we should change its range to be 21
# def my_function():
#This 20 in the range should be 21
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
#The bug here come when the dice_num become 6 and the last element of the list has index 5 so the interpreter generate error the 6 in the randint should be from 0 to 5 to cover all element
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
#The problem come from the condition of the if and elif that both of them don't cove the year of 1994 so we should change one range of them to cover this year
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
#The bug here is from the data types because the age will get and string input and it is used in the if statment as an int so that will generate a bug we should typecast the input data to be int
#Another bug is in the indentation in line 33 we should fix the indentation of the line
#Unexpected behavior of the print will be appear because we hadn't put f"String" we just put a "String" in the print function so it will print the {age} as it's no its value
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
#The unexpexted behavior come from line 40 becuase the operation in this line is comparing the input data with the word_per_page which is 0 so if the user input any number except 0 it will generate False which is 0 so the total words will be 0 too, to solve this problem we have to change the operator in line 40 to be = which is assign operator
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
#The unexpected behavior will be that the b_list will has one element on which is 26 because the line 50 was indent wrong it should have be if the for loop not outside it
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])