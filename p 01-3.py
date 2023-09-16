
def multiplication_table(x,y):
    multiplication_table = []
    for i in range(x,y):
        for j in range(1,13):
            multiplication_table.append(i * j)


    return multiplication_table

print(multiplication_table(2,5))