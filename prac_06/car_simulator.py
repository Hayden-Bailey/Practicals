"""
Car driving simulator
"""

from prac_06.car import Car


def main():
    print("Let's drive!")

    name = input("Enter your car name: ")
    car_simulator = Car(name, 100)

    print(car_simulator)

    menu_string = "Menu:\nd) drive\nr) refuel\nq) quit\nEnter your choice: "
    menu_input = input(menu_string).upper()
    while menu_input != "Q":
        if menu_input == "D":
            distance = int(input("How many kms do you wish to drive? "))
            if distance > car_simulator.fuel:
                print("{} drove {}km and ran out of fuel.".format(car_simulator.name, car_simulator.fuel))
            else:
                print("{} drove {}km".format(car_simulator.name, distance))
            car_simulator.drive(distance)
        elif menu_input == "R":
            refuel = int(input("How many units of fuel do you want to add to the car? "))
            car_simulator.add_fuel(refuel)
            print("{} units of fuel added to {}".format(refuel, car_simulator.name))
        else:
            print("Invalid choice: ")
        print(car_simulator)
        menu_input = input(menu_string).upper()

    print("Goodbye {} driver.".format(car_simulator.name))


main()
