"""Logic for brain_prime game"""

import prompt
from brain_games.tools.cli import welcome_user
from brain_games.tools.tools_numbers import number_random


def prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 1
    while count <= 3:
        number = number_random(1, 1000)
        print('Question:', number, sep=' ')
        answer = prompt.string('Answer: ')
        count_prime = 2
        result = 'yes'  # думаем, любое число простое, а доказываем обратное
        while count_prime <= number / 2:
            if number % count_prime != 0:
                count_prime += 1
            else:
                result = 'no'
                break

        if result == answer:
            print('Correct!')
            count += 1
            if count == 4:
                print('Congratulations, ', name, '!', sep='')
        else:
            print("'", answer, "' ", "is wrong answer ;(. Correct answer was '",
                  result, "'.\nLet's try again, " + name + '!', sep='')
            break
