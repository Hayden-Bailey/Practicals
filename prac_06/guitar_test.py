"""
Testing Guitar Class
"""

from prac_06.guitar import Guitar


def main():
    gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    test_guitar = Guitar("Test Guitar", 2009, 1500)

    gibson_age = gibson_guitar.get_age()
    test_age = test_guitar.get_age()

    print("{} get_age(): Expected 97 Got {}".format(gibson_guitar.name, gibson_age))
    print("{} get_age(): Expected 10 Got {}".format(test_guitar.name, test_age))

    gibson_vintage = gibson_guitar.is_vintage()
    test_vintage = test_guitar.is_vintage()

    print("{} is_vintage(): Expected True Got {}".format(gibson_guitar.name, gibson_vintage))
    print("{} is_vintage(): Expected False Got {}".format(test_guitar.name, test_vintage))


main()