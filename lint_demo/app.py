"""Module to calculate area of a circle."""

import math


def calculate_area(radius):

    """Calculate and print the area of a circle."""
    area = math.pi * radius * radius
    print(f"Area is {area}")


if __name__ == "__main__":
    calculate_area(5)
