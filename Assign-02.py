#!/usr/bin/env python3
#
# Created by: Nathan Araujo
# Created on: Oct 3 2022
# This program asks the user for the radius of
# a hemisphere and the units from the user. It then calculates the volume and surface area of the hemisphere.


import math


def main():
    # get the input for the radius from the user
    radius = float(input("Enter the radius of the hemisphere: "))
    # get the input for the unit of measurements from the user
    units = input("Enter the units you are using: ")

    # calculate the volume of the hemisphere
    volume = (2 / 3) * (math.pi) * radius**3
    # calculate the surface area of the hemisphere
    surface_area = 3 * (math.pi) * radius**2

    # display the volume of the hemisphere
    print("")
    print("The volume of the hemisphere is {:.2f}".format(volume), "{}^3".format(units))
    # display the surface area of the hemisphere
    print(
        "The surface area of the hemisphere is {:.2f}".format(surface_area),
        "{}^2".format(units),
    )
    
if __name__ == "__main__":
    main()
