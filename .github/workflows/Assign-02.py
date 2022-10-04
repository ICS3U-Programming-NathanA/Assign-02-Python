#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 3 2022
# This program asks the user for the radius of
# a hemisphere and the units from the user. It then calculates the volume and surface area of the hemisphere.


import math


def main():
    # get input for radius from the user
    radius = float(input("Enter the radius of the hemisphere: "))
    units = input("Enter the units you are using: ")
    # calculate the volume
    volume = (2 / 3) * (math.pi) * radius**3
    surface_area = 3 * (math.pi) * radius**2

    # display the circumference
    print("")
    print(
        "The volume of the hemisphere is = {:.2f}".format(volume), "{}^3".format(units)
    )
    print(
        "The surface area of the hemisphere is = {:.2f}".format(surface_area),
        "{}^3".format(units),
    )


if __name__ == "__main__":
    main()
