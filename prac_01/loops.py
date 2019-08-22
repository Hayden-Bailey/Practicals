for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
number_stars = int(input('How many stars? '))

for i in range(number_stars):
    print('*', end='')
print()

# D
for i in range(number_stars):
    for j in range(i):
        print('*', end='')
    print()