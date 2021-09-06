from collections import Counter

n = int(input())
numList1 = list(map(int, input().split()))
m = int(input())
numList2 = list(map(int, input().split()))


counter = Counter(numList1)

for i in range(m):
    if i == m - 1:
        print(counter[numList2[i]])
    else:
        print(counter[numList2[i]], end = ' ')
