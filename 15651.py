from itertools import product

n, m = map(int, input().split())
numList = [i for i in range(1, n + 1)]


for i in product(numList, repeat = m):
    print(' '.join(map(str, i)))

