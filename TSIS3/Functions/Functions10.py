

def unique(lst):
    sorted_lst = sorted(lst)
    final = [sorted_lst[0]]
    for i in range(1, len(lst)):
        if sorted_lst[i] != sorted_lst[i-1]:
            final.append(sorted_lst[i])
    print(final)


# unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    


