
def dividableNum(x,y):
    mylist = []
    for i in range(x,100):
        if i%y == 0 :
            mylist.append(i)
    return mylist


print(dividableNum(20,5))










