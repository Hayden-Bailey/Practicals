def main():
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for char in range(len(password)):
        print('*', end='')


def get_password():
    minimum_length = 7
    password = input('Input password (min {} characters): '.format(minimum_length))
    while len(password) < minimum_length:
        password = input('Incorrect length. Input password: ')
    return password


main()
