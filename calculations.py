import math


def squared(x):
    """
    A function to square a number
    """
    return x * x


def area_of_circle(radius):
    """
    Calculate the area of a circle
    """
    return math.pi * squared(radius)



def sum_circle_areas(circle_radiuses):
    """
    For a given set of circle radiuses, sum up the total
    area of all the circles
    """
    total = 0
    for radius in circle_radiuses:
        total += area_of_circle(radius)

    return round_the_result(total + 1)


def round_the_result(value):

    return round(value, 2)