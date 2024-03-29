"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input('Sales amount ($): '))

if sales < 1000:
    bonus = sales * .1
else:
    bonus = sales * .15

print('Bonus is: ${:.2f}'.format(bonus))

# Part 2

sales = float(input('Sales amount ($): '))
while sales >= 0:
    if sales < 1000:
        bonus = sales * .1
    else:
        bonus = sales * .15
    print('Bonus is: ${:.2f}'.format(bonus))
    sales = float(input('Sales amount ($): '))
