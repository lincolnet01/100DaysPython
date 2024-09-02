# Program that can generate math problems. 

import random
import time

def main():

    MIN_NUMBER = 3
    MAX_NUMBER = 12
    OPERATORS = ["+", "-", "*"]

    def problemGenerator():
        left_Operand = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_Operand = random.randint(MIN_NUMBER, MAX_NUMBER)
        operator = random.choice(OPERATORS)
        expr = str(left_Operand) + right_Operand + str(right_Operand) 
        answer = eval(expr)
        return expr, answer
    
    expr, answer = problemGenerator()

    print(expr)
    print(answer)

if __name__ == '__main__':
    main()

