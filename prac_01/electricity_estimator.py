"""
Electricity Bill Calculator
"""
print('Electricity bill estimator')

price_per_hour = float(input('Enter cents per kWh (c): '))
daily_use = float(input('Enter daily use in kWh (hrs): '))
number_days = int(input('Enter number of billing days: '))

print('Estimated bill: ${}'.format((price_per_hour / 100) * daily_use * number_days))