
string = "lool"

def ispalin(string):
    a = True
    for i in range(0, len(string)//2):
        if string[i] != string[len(string)-i-1]:
            a = False
            break
    if a == True:
        print("Palindrome")
    else:
        print("No")

ispalin(string)