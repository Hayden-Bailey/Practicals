"""
Quick Pick Lottery Ticket Generator
"""

import random


def main():
    pick_amount = int(input("How many quick picks? "))

    for i in range(pick_amount):
        random_picks = []
        generate_picks(random_picks)
        random_picks.sort()
        print(" ".join(['{:2}'.format(number) for number in random_picks]))
        random_picks.clear()


def generate_picks(random_picks):
    for index in range(6):
        random_number = random.randint(1, 45)
        while random_number in random_picks:
            random_number = random.randint(1, 45)
        random_picks.append(random_number)


main()
