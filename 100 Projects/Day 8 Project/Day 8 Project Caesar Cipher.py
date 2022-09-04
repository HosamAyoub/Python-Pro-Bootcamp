alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

decoded_word = ""

def ecrypt(plain_text, shift_amount):
    encrypted_word = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        if (position + shift_amount) < len(alphabet):
            encrypted_word += alphabet[position + shift_amount]
        else:
            encrypted_word += alphabet[position + shift_amount - len(alphabet)]
    print(encrypted_word)
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

ecrypt(text, shift)