"""
List Exercises
"""

input_number = int(input('Number 1: '))
numbers = []
index = 1
while input_number >= 0:
    numbers.append(input_number)
    index += 1
    input_number = int(input('Number {}: '.format(index)))


print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("Username: ")
if user_name in usernames:
    print("Access Granted")
else:
    print("Access Denied")