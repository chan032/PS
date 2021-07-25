total1, total2 = map(int, input().split())  # [1, 50 0000]


infoDict = dict()
for i in range(total1):
    name1 = input()
    infoDict.setdefault(name1, None)
answer = []
for i in range(total2):
    name2 = input()
    if name2 in infoDict.keys():
        answer.append(name2)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
