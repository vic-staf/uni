
def histogram(lst):
    for i in range(len(lst)):
        for j in range(lst[i]):
            print("*", end="")
        print("")


# histogram([4, 8, 6])