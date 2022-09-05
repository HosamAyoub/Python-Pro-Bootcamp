programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
"Function": "A piece of code that you can easily call over and over again."
}

#Retrieving item from dictionary
# print(programming_dictionary["Bug"])

#Add element to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Create empty dictionary
empty_dictionary = {}

#wipe an exesting dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")