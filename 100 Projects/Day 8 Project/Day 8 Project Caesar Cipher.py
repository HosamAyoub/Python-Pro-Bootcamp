alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode': 
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        if position + shift_amount < len(alphabet):
            new_position = position + shift_amount
        else:
            new_position =  position + shift_amount - len(alphabet)
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))   


caesar(text, shift, direction)