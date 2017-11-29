num = int(input())
things = []
for x in range(num):
    things.append(input())
for x in things:
    if len(x) > 10:
        print(x[0] + str(len(x) - 2) + x[-1])
    else:
        print(x)
