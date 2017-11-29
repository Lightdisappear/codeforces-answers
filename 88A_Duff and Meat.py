num = int(input())
a = []
b = []
for x in range(num):
    temp = input().split(" ")
    b.append(int(temp[0]))
    a.append(int(temp[1]))
    pass

cost = 0
lowestday = num
day = num

while len(a[:lowestday]) > 0:
    c = a[:lowestday]
    lowestprice = min(c)
    lowestday = a.index(min(c))
    #print("lowestprice", lowestprice)
    #print("lowestday", lowestday)
    if a[lowestday:]:
        cost += sum([lowestprice * x for x in b[lowestday:day]])
        # print(a[lowestday:])
        # print(cost)
        pass
    day = lowestday
    # print(a[:lowestday])
    pass

print(cost)
