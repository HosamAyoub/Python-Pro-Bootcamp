#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    name = name.rstrip('\n')
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(letter.replace("[name]", name))