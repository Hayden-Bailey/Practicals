def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for char in range(len(password)):
        print('*', end='')


def get_password():
    password = input('Input password (min 7 characters): ')
    while len(password) <= 6:
        password = input('Incorrect length. Input password: ')
    return password


main()
