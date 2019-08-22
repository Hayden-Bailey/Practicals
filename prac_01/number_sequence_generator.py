"""
Menu-Driven Number Sequence Generator
"""

import math

number_x = int(input('Enter a number x: '))
number_y = int(input('Enter a number y: '))

menu_string = 'i. Show the even numbers from x to y.\nii. Show the odd numbers from x to y.\niii. Show the ' \
              'squares from x to y.\niv. Exit the program.\n\n>>> '

choice = input(menu_string).upper()

while choice != 'IV':
    if choice == 'I':
        if number_x % 2 == 0:
            for i in range(number_x, number_y + 1, 2):
                print(i)
        else:
            for i in range(number_x + 1, number_y + 1, 2):
                print(i)
    elif choice == 'II':
        if number_x % 2 == 1:
            for i in range(number_x, number_y + 1, 2):
                print(i)
        else:
            for i in range(number_x + 1, number_y + 1, 2):
                print(i)
    elif choice == 'III':
        for i in range(number_x, number_y + 1):
            print('{:.2f}'.format(math.sqrt(i)))
    else:
        print('Invalid option.')
    choice = input(menu_string).upper()

print('Thank you!')
