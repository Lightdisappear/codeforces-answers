a = int(input())
b = [int(x) for x in input().split()]

min1 = a
minindex = -1
for i in range(9):
    if b[i] <= min1:
        min1 = b[i]
        minindex = i

if minindex == -1:
    print("-1")
else:
    count = a // min1
    left = a % min1 + min1
    time = 0
    for y in range(count):
        key = 1
        for x in range(8, minindex - 1, -1):
            if b[x] < left:
                print(x + 1, end="")
                left = left - b[x] + min1
                time += 1
                key = 0
                break
                pass
            pass
        print("key=", key)
        if key == 1:
            break
    print(str(minindex + 1) * (count - time))
