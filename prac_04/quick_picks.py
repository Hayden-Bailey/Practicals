"""
Quick Pick Lottery Ticket Generator
"""

import random

RANDOM_PICKS = []


def main():
    pick_amount = int(input("How many quick picks? "))

    for i in range(pick_amount):
        generate_picks()
        RANDOM_PICKS.sort()
        for number in RANDOM_PICKS:
            print('{:2}'.format(number), end=' ')
        print('')
        RANDOM_PICKS.clear()


def generate_picks():
    for index in range(6):
        random_number = random.randint(1, 45)
        while random_number in RANDOM_PICKS:
            random_number = random.randint(1, 45)
        RANDOM_PICKS.append(random_number)


main()
