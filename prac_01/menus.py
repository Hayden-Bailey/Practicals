"""
Menus Practice
"""

user_name = input('Enter name: ')
menu_string = '(H)ello\n(G)oodbye\n(Q)uit\n\n>>> '

choice = input(menu_string).upper()

while choice != 'Q':
    if choice == 'H':
        print('Hello', user_name)
    elif choice == 'G':
        print('Goodbye', user_name)
    else:
        print('Invalid option.')
    choice = input(menu_string).upper()

print('Finished.')
