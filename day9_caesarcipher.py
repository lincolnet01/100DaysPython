print('''
Caesar Cipher, by Linc
''')

try:
    import pyperclip
except ImportError:
    print("Error import pyperclip")
    pass # Please intall pyperclip (optional)


SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translated = ""

# Let the user decide if they want to encrypt or decrypt a message
while True:
    print("Do you want to (e)ncrypt or (d)ecrypt ? ")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print('Please enter the letter e or d. ')

# Ask for the key
while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (1 to  {})".format(maxKey))
    key = input("> ")
    if not key.isdecimal():
        continue
    if 1 <= int(key) <= maxKey:
        key = int(key)
        break

# Ask for the message
print("Enter the message to {}".format(mode))
message = input("> ").upper() # Caesar cipher only works on uppercase letters:

#Encrypt/Decrypt each symbol in the message:
for char in message:
    if char in SYMBOLS:
        num = SYMBOLS.find(char)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += char

# Display the ecrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed text copied to clipboard.".format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed        
