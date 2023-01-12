from random import randint


GUIDE = 'What number is missing in the progression?'


def generate_round():
    progression = list(range(randint(1, 10), randint(30, 99), randint(2, 5)))
    progression = progression[:randint(10, 20)]
    random_index = randint(0, len(progression) - 1)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    progression = list(map(str, progression))
    progression = ' '.join(progression)
    correct_answer = str(correct_answer)
    return progression, correct_answer
