
from itertools import permutations


def str_permuts(string):
    lst = permutations(string)
    for i in lst:
        print(i)

# str_permuts("abc")
        
