import math
import time

lst = [1, 2, 3, 4, 5]   


def multiply(lst):
    product = 1
    for i in lst:
        product = product * i

    return product


print(multiply(lst))