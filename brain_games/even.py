"""Logic for brain_even"""


import random
import prompt


def even():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        num = number_random()
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


def number_random():
    start = 1
    finish = 100
    number = random.randint(start, finish)
    return number
