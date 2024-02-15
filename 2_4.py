a = int(input())
b = int(input())

def squares(start, stop):
    for i in range(start, stop + 1):
        yield i * i

c = squares(a, b)
for i in c:
    print(i)