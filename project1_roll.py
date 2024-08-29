import random

def main():

    # Get the number of players
    while True:
        print('Enter the number of players (2-4)')
        numPlayer = input('> ')
        if numPlayer.isdecimal() and 2 <= int(numPlayer) <= 4:
            numPlayer = int(numPlayer)
            break
        else:
            continue
    
    # Manage players turn
    while True:
        playerScores = [('player1', 0), ('player2', 0)]
        for i in range(numPlayer):
            print('Player', i + 1, 'turn has started')
            currentScore = 0
            while True:
                print('Would you like to roll ? (y/n)')
                response = input('> ')
                if response.lower().startswith('y'):
                    roll = random.randint(1, 9)
                    if roll == 1:
                        print('You rolled a 1. Your turn is done!')
                        print()
                        print('You total score is: {}'.format(playerScores[i][i]))
                        continue
                    else:
                        print('You rolled {}'.format(roll))
                        currentScore += roll
                        print()
                        print('Your current score is: {}'.format(currentScore))
                elif response.lower().startswith('n'):
                    break

if __name__ == '__main__':
    main()