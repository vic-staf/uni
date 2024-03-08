tuple = (True, True, True, False, False)

def isalltrue(tuple):
    a = True
    for i in tuple: 
        if i != True: a = False
    return a
print(isalltrue(tuple))
