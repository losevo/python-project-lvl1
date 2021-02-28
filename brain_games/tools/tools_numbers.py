""" Random staff tools"""

import random


def number_random(start, finish):
    number = random.randint(start, finish)
    return number


def operator_random():
    clap = random.choice(['+', '-', '*'])
    return clap
