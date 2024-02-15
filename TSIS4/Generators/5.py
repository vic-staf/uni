def generator(n):
    for i in range(n, -1, -1):
            yield i



n = int(input())
x = generator(n)
for i in x:
    print(i, sep = ", ")