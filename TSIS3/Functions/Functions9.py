import math

from itertools import permutations  

def volume_sphere(radius):
    print((radius ** 3) * 4 * math.pi / 3)
    return (radius ** 3) * 4 * math.pi / 3


# volume_sphere(10)