a, b = input().split()
a = list(a)
b = list(b)

answer = 51
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            count += 1

    answer = min(answer, count)

print(answer)

