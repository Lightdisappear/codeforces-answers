a = [x for x in range(100)]
key = 1
for x in a:
    for a in range(x):
        if a == 4:
            print(a)
        if x == 20:
            key = 0
            pass
        pass
    if key == 0:
        break
    pass
