""" Logic for brain-progression game """

import prompt
from brain_games.tools.cli import welcome_user
from brain_games.tools.tools_numbers import number_random


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    count = 1
    while count <= 3:
        start_number = number_random(1, 100)
        diff = number_random(1, 10)
        stop_progression = number_random(6, 10)
        count_pr = 1
        start_pr = str(start_number)
        hidden_count = number_random(1, stop_progression - 1)
        while count_pr < stop_progression:
            if count_pr == hidden_count:
                start_pr = str(start_pr) + ' .. '
                result = start_number + diff * count_pr
            else:
                start_pr = start_pr + ' ' + str(start_number + diff * count_pr)
            count_pr += 1
        print('Question: ' + start_pr)
        answer = prompt.string('Answer: ')
        if str(result) == answer:
            print('Correct!')
            count += 1
            if count == 4:
                print('Congratulations, ', name, '!', sep='')
        else:
            print("'", answer, "' ", "is wrong answer ;(. Correct answer was '",
                  result, "'.\nLet's try again, " + name + '!', sep='')
            break
