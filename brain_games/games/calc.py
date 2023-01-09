import random
from random import randint

GUIDE = 'What is the result of the expression?'


def generate_round():
    operands = ['+', '-', '*']
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    random_op = random.choice(operands)
    if random_op == '+':
        correct_answer = first_number + second_number
    elif random_op == '-':
        correct_answer = first_number - second_number
    elif random_op == '*':
        correct_answer = first_number * second_number
    question = f'{first_number} {random_op} {second_number}'
    return question, str(correct_answer)
