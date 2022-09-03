import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
display = []
print(logo)
for iterator in chosen_word:
    display.append("_")

print(f"Pssst, the solution is {chosen_word}.")
#while
while lives != 0:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = guess
    lives -= 1
    #Check if it was guessed before
    if guess in display:
        print(f"You already gussed that {guess}.")
        lives += 1
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You have guessed {guess}, that's not in the word.")
        print("Be careful you lose a life.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        print("You win.")
        break;
    if lives == 6:
        print(stages[lives])
    else:
        print(stages[lives])

if lives == 0:
    print("You lose.")