
def oddsEvenNumbers(x,y):
    evenlist = []
    oddlist  = []
    for i in range(x,y):
        if i %2 == 0:
            evenlist.append(i)
        elif i %2 != 0:
            oddlist.append(i)

    return evenlist,oddlist

even,odd=oddsEvenNumbers(0,10)





