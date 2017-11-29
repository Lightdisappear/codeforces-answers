a, b = [int(x) for x in input().split(" ")]

d = 0
if b > a:
    print(-1)
else:
    c = int(a / 2) + a % 2
    if c % b != 0:
        d = b - c % b
    print(c + d)
