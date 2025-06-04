from collections import Counter
def pickingNumbers(a):
    count = Counter(a)
    print(count)
    max_length = 0
    for num in count:
        max_length = max(max_length, count[num] + count[num + 1])
    return max_length

a=[4,5,6,3,3,1]
print(pickingNumbers(a))
