
def multiplication_table(x,y):
    multiplication_table  = []
    for i in range(x,y):
        for j in range(1,12):
            if i * x == 0 and i % y == 0:
                multiplication_table.append(i)


    return multiplication_table

print(multiplication_table(2,3))