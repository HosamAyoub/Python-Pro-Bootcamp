alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encrypted_word = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        if (position + shift_amount) < len(alphabet):
            encrypted_word += alphabet[position + shift_amount]
        else:
            encrypted_word += alphabet[position + shift_amount - len(alphabet)]
    print(f"The encoded text is {encrypted_word}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
    decoded_word = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        decoded_word += alphabet[position - shift_amount]
    print(f"The encoded text is {decoded_word}")


#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)