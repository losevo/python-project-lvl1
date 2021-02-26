""" Random staff tools"""

import random


def number_random():
    start = 1
    finish = 100
    number = random.randint(start, finish)
    return number


def operator_random():
    clap = random.choice(['+', '-', '*'])
    return clap
