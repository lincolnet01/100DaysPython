import random
from collections import Counter
from typing import List, Dict

# Constants
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def main() -> None:
    """
    Main function to simulate the Birthday Paradox.
    """
    print('''
    --------------------------------------------
    Birthday Paradox, by Linc
    This program simulates the birthday paradox
    --------------------------------------------
          ''')

    # Get the number of simulations from the user
    numberOfBirthdays = get_numberOfBirthdays()

    # Run the first simulate and get results
    values = birthday_simulation(numberOfBirthdays)
    duplicates = values['duplicates']
    birthdays = values['birthdays']
    birthdays_string = ', '.join(birthdays)

    # Display the randomly generated birthdays
    print('--------------------------------------------')
    print(f'Here are {numberOfBirthdays} birthdays:')
    print(birthdays_string)
    print('--------------------------------------------')

    # Display duplicates
    if duplicates:
        print(f"In this simulation, multiple people have the same birthday on: {', '.join(duplicates)}")
    else:
        print('All birthdays are unique')

    # Run 100,000 simulations and display the results
    run_simulations(numberOfBirthdays)


def get_numberOfBirthdays() -> int:
    """
    Prompt the user to input the number of birthdays to generate.
    Returns:
        int: The number of birthdays to generate.
    """
    while True:
        print('How many birthdays do you want to generate? (Max 100)')
        numberOfBirthdays = input('> ')
        if numberOfBirthdays.isdigit() and 1 <= int(numberOfBirthdays) <= 100:
            return int(numberOfBirthdays)
        else:
            print('Please enter a number between 1 and 100')


def birthday_simulation(numberOfBirthdays: int) -> Dict[str, List[str]]:
    """
    Simulate random birthdays and find duplicates.

    Args:
        numberOfBirthdays (int): The number of birthdays to simulate.

    Returns:
        Dict[str, List[str]]: A dictionary containing duplicates and all birthdays.
    """
    birthdays = []

    # Generate random birthdays
    for _ in range(numberOfBirthdays):
        day_of_year = random.randint(1, 365)

        for i, days in enumerate(DAYS_IN_MONTH):
            if day_of_year <= days:
                month = MONTHS[i]
                day = day_of_year
                birthdays.append(f'{month} {day}')
                break
            day_of_year -= days

    # Count duplicates
    birthday_counts = Counter(birthdays)
    duplicates = [item for item, count in birthday_counts.items() if count > 1]

    return {'duplicates': duplicates, 'birthdays': birthdays}


def run_simulations(numberOfBirthdays: int) -> None:
    """
    Run 100,000 simulations to calculate the probability of matching birthdays.

    Args:
        numberOfBirthdays (int): The number of birthdays to simulate in each run.
    """

    # Run the simulation
    i_values = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    simMatch = 0
    print('--------------------------------------------')
    print("Let's run another 100,000 simulations")
    print('Press ENTER to begin...')
    input()
    for i in range(100000):
        if i in i_values:
            print(f'{i} simulations run...')
        values = birthday_simulation(numberOfBirthdays)
        if values['duplicates']:
            simMatch += 1

    # Display results
    probability = (simMatch / 100000) * 100
    print(f'''
        --------------------------------------------------------------------
        Out of 100,000 simulations of {numberOfBirthdays} people, there was a
        matching birthday in that group {simMatch} times. This means
        that {numberOfBirthdays} people have a {probability:.2f}% chance of
        having a matching birthday in their group.
        That's probably more than you would think!
        -------------------------------------------------------------------
    ''')


if __name__ == '__main__':
    main()