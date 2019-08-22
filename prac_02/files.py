"""
Do-From-Scratch Files
"""
NAME_FILE = 'name.txt'
NUMBERS_FILE = 'numbers.txt'
MANY_NUMBERS_FILE = 'many numbers.txt'

# Q1
name_file_1 = open(NAME_FILE, 'w')
user_name = input('Enter your name: ')
name_file_1.write(user_name)
name_file_1.close()

# Q2
name_file_2 = open(NAME_FILE, 'r')
read_name = name_file_2.read().strip()
print('Your name is:', read_name)
name_file_2.close()

# Q3
number_file = open(NUMBERS_FILE, 'r')
first_number = int(number_file.readline())
second_number = int(number_file.readline())
total = first_number + second_number
print('Total is:', total)
number_file.close()

# Q4

many_numbers = open(MANY_NUMBERS_FILE, 'r')

total = 0
for line in many_numbers:
    number = int(line)
    total += number
print('Total is:', total)
many_numbers.close()
