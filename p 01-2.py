def dividedByXY(x,y):
    dividedlist  = []
    for i in range(1,100):
        if i % x == 0 and i % y == 0:
            dividedlist.append(i)

    return dividedlist

print(dividedByXY(2,3))