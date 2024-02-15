def generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i



n = int(input())
x = generator(n)
for i in x:
    print(i, end = ", ")