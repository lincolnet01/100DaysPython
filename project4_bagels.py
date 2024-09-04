import random, sys

def main():

    NUMBER_OF_GUESSES = 10

    print('''
        ========================================================== 
        Bagels a deductive logic game by Linc 
        I am thinking of a 3-digit number. Try to guess what it is.
        Here are some clues:
        When I say:  | That means:
        Pico         | One digit is correct but in the wrong position.
        Fermi        | One digit is correct and in the right position.
        Bagels       | No digit is correct.
        ===========================================================
          ''')
    
    while True:
        input('press <Enter> to start... ')
        
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        random.shuffle(DIGITS)
        num = DIGITS[0:3]
        num = ''.join(num)
        
        print('I have thought up a number.')
        print('You have 10 guesses to get it.')
        for i in range(NUMBER_OF_GUESSES):
            while True:
                print('Guess #{}:'.format(i+1))
                guess = input('> ')
                if guess.isdigit() and len(guess) == 3:
                    break
            clues = []
            for digit in guess:
                if digit in num:
                    # Check if the digit is in the correct position.
                    if guess.index(digit) == num.index(digit):
                        clues.append('Femi')
                    else:
                    # Print if the digit is not in correct place.
                        clues.append('Pico')
                else:
                    clues.append('Bagels')
            if clues == ['Femi', 'Femi', 'Femi']:
                print('You got it in {} guesses!'.format(i + 1))
                break
            random.shuffle(clues)
            print(' '.join(clues))
        response = input('Do you want to play again (yes / no): ')
        if response.startswith('n'):
            print('Thanks for playing!')
            sys.exit()
        if response.startswith('y'):
            print('-------------------------------------------------')
            continue

        break

if __name__ == '__main__':
    main()