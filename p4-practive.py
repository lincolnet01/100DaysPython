import random

NUM_DIGIT = 3
NUMBER_OF_GUESSES = 10

def main():
    while True:
        print('I am thinking of {} digit number, can you guess'.format(NUM_DIGIT))
        secretNumber = secretNumGenerator()
        for i in range(NUMBER_OF_GUESSES):
            while True:
                guess = input('Guess #{}: '.format(i + 1))
                if len(guess) == NUM_DIGIT and guess.isdecimal():
                    break
                else:
                    continue
            if guess == secretNumber:
                print('You got it')

            clues = getClues(secretNumber, guess)
            print(clues)

def secretNumGenerator():

    numberList = list('0123456789')
    random.shuffle(numberList)
    secretNumber = numberList[0:NUM_DIGIT]
    secretNumber = ''.join(secretNumber)

    return secretNumber

def getClues(secretNumber, guess):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNumber[i]:
            clues.append('Fermi')
        if guess[i] in secretNumber:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ' '.join(clues)
            
if __name__ == '__main__':
    main()