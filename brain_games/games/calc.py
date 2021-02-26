""" Logic for calculator game """

import prompt
from brain_games.tools.cli import welcome_user
from brain_games.tools.tools_numbers import operator_random
from brain_games.tools.tools_numbers import number_random


op = {"+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "*": lambda x, y: x * y}


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 1
    while count <= 3:
        first_number = number_random()
        second_number = number_random()
        sign = operator_random()
        result = op[sign](first_number, second_number)
        print('Question:', str(first_number), sign, str(second_number), sep=' ')
        answer = prompt.string('Answer: ')
        if str(result) == answer:
            print('Correct!')
            count += 1
            if count == 4:
                print('Congratulations, ' + name + '!')
        else:
            print("'", str(answer), "' is wrong answer ;( Correct answer was '",
                  str(result), "'", sep='')
            print("Let's try again, " + name + "!")
            break
