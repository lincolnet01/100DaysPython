import random

def main():

    # Get the number of players
    while True:
        print('Please enter the number of players (2-4)')
        numPlayer = input('> ')
        if numPlayer.isdigit() and 2 <= int(numPlayer) <= 4:
            numPlayer = int(numPlayer)
            break
        else:
            continue
    
    # Manage players turn and update the score
    playerScores = [0 for _ in range(numPlayer)]
    max_score = 50
    min_value = 1
    max_value = 6
    print(playerScores)
    while max(playerScores) < max_score:
        for player_idx in range(numPlayer):
            print('Player', player_idx + 1, 'turn has started')
            currentScore = 0
            while True:
                print('Would you like to roll ? (y/n)')
                response = input('> ')
                if response.lower().startswith('y'):
                    roll = random.randint(min_value, max_value)
                    if roll == 1:
                        print('You rolled a 1. Your turn is done!')
                        print()
                        print('Your total score is: {}'.format(playerScores[player_idx]))
                        print()
                        break
                    else:
                        print('You rolled {}'.format(roll))
                        currentScore += roll
                        print()
                        print('Your current score is: {}'.format(currentScore))
                elif response.lower().startswith('n'):
                    playerScores[player_idx] += currentScore
                    print('You total score is: {}'.format(playerScores[player_idx]))
                    print()
                    break
        
    # Find the winner
    max_score = max(playerScores)
    winner_idx = playerScores.index(max_score)
    print('Player {} won with a score of {}'.format(winner_idx + 1, max_score))

if __name__ == '__main__':
    main()