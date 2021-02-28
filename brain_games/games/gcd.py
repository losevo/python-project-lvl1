""" Logic for brain-gcd game """

import prompt
from brain_games.tools.cli import welcome_user
from brain_games.tools.tools_numbers import number_random


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 1
    while count <= 3:
        first_number = number_random(1, 100)
        second_number = number_random(1, 100)
        print('Question:', first_number, second_number, sep=' ')
        answer = prompt.string('Answer: ')
        while first_number != second_number:
            if first_number > second_number:
                first_number = first_number - second_number
            else:
                second_number = second_number - first_number

        if str(first_number) == answer:
            print('Correct!')
            count += 1
            if count == 4:
                print('Congratulations, ', name, '!', sep='')
        else:
            print("'", answer, "' ", "is wrong answer ;(. Correct answer was '",
                  first_number, "'.\nLet's try again, " + name + '!', sep='')
            break
