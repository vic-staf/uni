def squares(a,b):
    for i in range(a,b+1,1):
        yield i * i


a, b = map(int, input().split())
c = squares(a,b)
for i in c:
    print(i)