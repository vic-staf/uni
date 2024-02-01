

def primes(lst):
    i = 0
    while i < len(lst):
        deleted = False
        for j in range(2, lst[i]):
            if lst[i] % j == 0:
                lst.remove(lst[i])
                deleted = True
                break
        if not deleted:
            i += 1
    print(lst)

# primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])