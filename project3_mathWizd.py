# Program that can generate math problems. 

import random
import time

MIN_NUMBER = 3
MAX_NUMBER = 12
OPERATORS = ["+", "-", "*"]

def main():

    NUMBER_OF_PROBLEMS = 10

    input('Please type <Enter> to start')
    print('--------------------------')

    wrongAnswers = 0

    startTime = time.time()

    for i in range(NUMBER_OF_PROBLEMS):
        exp, answer = problemGenerator()
        while True:
            userAnswer = input('Problem #{}: {} = '.format(i+1, exp))
            if userAnswer == str(answer):
                break
            wrongAnswers += 1

    endTime = time.time()
    totlaTime = round(endTime - startTime, 2)

    print('-------------------------')
    print('Well done, you have finished in: {}'.format(totlaTime))  
    print('You missed: {} times'.format(wrongAnswers)) 
    print('-------------------------') 

def problemGenerator():
    left_Operand = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_Operand = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)
    expr = str(left_Operand) + ' ' + operator + ' ' + str(right_Operand) 
    answer = eval(expr)
    return expr, answer

if __name__ == '__main__':
    main()

