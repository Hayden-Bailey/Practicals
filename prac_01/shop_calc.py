"""
Shop Calculator
"""

total = 0
number_of_items = int(input('Number of items: '))
while number_of_items < 0:
    number_of_items = int(input('Invalid number of items!\nNumber of items: '))

for i in range(number_of_items):
    item_price = float(input('Input item {} price ($): '.format(i)))
    total += item_price

if total > 100:
    total *= 0.9

print('Total price of {} items is ${:.2f}'.format(number_of_items, total))
