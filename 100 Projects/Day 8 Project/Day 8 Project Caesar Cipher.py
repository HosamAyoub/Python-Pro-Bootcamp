from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode': 
        shift_amount *= -1
    for letter in plain_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            if position + shift_amount < 26:
                new_position = position + shift_amount
            else:
                new_position =  (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction} text is {end_text}")

print(logo)
while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if (direction == 'encode' or direction == 'decode'):
        caesar(text, shift, direction)
    else:
        print("Please enter 'encode' or 'decode' next time.")
    if input("Type 'no' to exit program.") == 'no':
        print("Goodbye!")
        break