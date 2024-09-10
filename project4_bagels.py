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
    while True: # Main game loop
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


