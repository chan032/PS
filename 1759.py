from itertools import combinations

l, c = map(int, input().split())
chars = list(input().split())
moList = []
jaList = []
for char in chars:
    if char in ['a', 'e', 'i', 'o', 'u']:
        moList.append(char)
    else:
        jaList.append(char)
# print(chars)

allCase = []
for j in range(2 , l):
    for jaCase in combinations(jaList, j):
        for moCase in combinations(moList, l - j):
            tmp = list(jaCase) + list(moCase)
            tmp.sort()
            tmp = ''.join(tmp)
            allCase.append(tmp)
allCase.sort()
print('\n'.join(allCase))


