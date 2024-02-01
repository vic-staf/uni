

def spy_game(lst):
    cnt = 0
    for i in range(len(lst)):
        if cnt == 1 or cnt == 0:
            if lst[i] == 0:
                cnt += 1
        elif cnt == 2:
            if lst[i] == 7:
                print(True)
                return True
    print(False)
    return False


# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])