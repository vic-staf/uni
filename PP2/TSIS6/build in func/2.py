word = "WorD"

def low_upp(word):
    lower = 0
    upper = 0
    for i in word:
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    return lower, upper

print(low_upp(word))
