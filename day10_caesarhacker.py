print('''
Caesar Cipher Hacker, by Linc
''')

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Ask for the message
print("Enter the message to decrypt")
message = input("> ").upper() # Caesar cipher only works on uppercase letters:

#Decrypt each symbol in the message:
for key in range(1, len(SYMBOLS)):
    translated = ""
    for char in message:
        if char in SYMBOLS:
            num = SYMBOLS.find(char)
            num = num - key
            if num < 0:
                num += len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += char

# Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))

