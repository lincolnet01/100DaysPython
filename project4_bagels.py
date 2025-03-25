import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''=====================================================
===  Welcome to Bagels, a deductive logic game.   ===
=====================================================

 I am thinking of a {}-digit number with no repeated digits.
 You have {} guesses to guess what it is. Here are some clues:

 When I say | It means
----------------------
 Pico       | One digit is correct but in the wrong position
 Fermi      | One digit is correct and in the right position.
 Bagels     | No digit is correct.
----------------------

 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.

          '''.format(NUM_DIGITS, MAX_GUESSES))

    while True:  # Main game loop
        secretNum = getSecretNum()
        input("Press <Enter> to start ")
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('''

                --------------------------------------------
                Game over! You ran out of guesses!
                The correct anser is", {}
                --------------------------------------------

                      '''.format(secretNum))
        print('Do you want to play again ? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!!!')


def getSecretNum():
    secreNum = ''
    numbers = list('0123456789')
    random.shuffle(numbers)

    for i in range(NUM_DIGITS):
        secreNum += numbers[i]
    return secreNum


def getClues(guess, secretNum):
    clues = []
    if guess == secretNum:
        return '''
                      
        --------------------------------------------
        Well done, you got it! :)
        --------------------------------------------

        '''

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()

# Exploring the Program
# Try to find the answers to the following questions. Experiment with some modifications to the code and rerun the program to see what effect the changes have.

# What happens when you change the NUM_DIGITS constant?
# What happens when you change the MAX_GUESSES constant?
# What happens if you set NUM_DIGITS to a number larger than 10?
# What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?
# What error message do you get if you delete or comment out numGuesses = 1 on line 34?
# What happens if you delete or comment out random.shuffle(numbers) on line 62?
# What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?
# What happens if you comment out numGuesses += 1 on line 44?

# More info on this program: https://inventwithpython.com/bigbookpython/project1.html
