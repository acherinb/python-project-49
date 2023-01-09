from prompt import string

num_rounds = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GUIDE)
    for _ in range(num_rounds):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
