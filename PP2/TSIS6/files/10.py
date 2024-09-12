'''import os
import re
a = "RARDD fndfj09-03-2024ghglk jj"
with open(r"file.txt", "w") as f:
    f.write(a)

reg = re.search(r'\d\d-\d\d-\d\d\d\d', a)
print(reg[0] if reg else "Not found" ) '''
'''
def generator(n):
    for i in range(n+1):
        yield i*i

n = int(input())

x = generator(n)
for i in x:
    print(i)
'''

def generator():
    yield 1
    yield 2
    yield 3

x = generator()
for i in x:
    print(i)





