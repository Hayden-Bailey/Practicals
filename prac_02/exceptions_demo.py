try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator is 0. Re-enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#    print("Cannot divide by zero!")
print("Finished.")

"""
Question 1: ValueError will occur when a non-number (incl. floats) is entered.
Question 2: ZeroDivisionError when the denominator is a zero.
Question 3: Create a sequence to check for 0 input before the equation.
"""
