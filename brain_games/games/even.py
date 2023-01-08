from random import randint


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(-99, 99)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
