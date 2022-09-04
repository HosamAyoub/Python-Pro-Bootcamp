alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))   

def caesar(plain_text, shift_amount, cipher_direction):
    if direction == 'encode':
        encrypted_word = ''
        for letter in plain_text:
            position = alphabet.index(letter)
            if (position + shift_amount) < len(alphabet):
                encrypted_word += alphabet[position + shift_amount]
            else:
                encrypted_word += alphabet[position + shift_amount - len(alphabet)]
        print(f"The encoded text is {encrypted_word}")
    elif direction == 'decode':
        decoded_word = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            decoded_word += alphabet[position - shift_amount]
        print(f"The decoded text is {decoded_word}")

caesar(text, shift, direction)