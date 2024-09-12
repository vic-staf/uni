

def has_33(lst):
    for i in range(len(lst) - 1):
        if lst[i] == 3:
            if lst[i + 1] == 3:
                print(True)
                return True
    print(False)
    return False


# has_33([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3])
# 8



