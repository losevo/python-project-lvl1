"""Logic for brain_even"""

import prompt
from brain_games.tools.cli import welcome_user
from brain_games.tools.tools_numbers import number_random


def even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        num = number_random(1, 100)
        print('Question: ' + str(num))
        answer = prompt.string('Answer: ')
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        if result == answer:
            print('Correct!')
            count += 1
            if count == 4:
                print('Congratulations, ', name, '!', sep='')
        else:
            print("'", answer, "' ", "is wrong answer ;(. Correct answer was '",
                  result, "'.\nLet's try again, " + name + '!', sep='')
            break
