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
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])