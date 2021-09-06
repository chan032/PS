def w(n1, n2, n3):
    dpTable = [[[0] * (n1 + 1) for _ in range(n2 + 1)] for __ in range(n3 + 1)]
    dpTable[1]
    for i in range(n1):
        for j in range(n2):
            for k in range(n3):

                if n1 <= 0 or n2 <= 0 or n3 <= 0:
                    dpTable[i][j][k] = 1
                elif n1 > 20 or n2 > 20 or n3 > 20:
                    dpTable[i][j][k] = dpTable[20][20][20]
                elif n1 < n2 and n2 < n3:
                    dpTable[i][j][k] = dpTable[n1][n2][n3 - 1] + dpTable[n1][n2 - 1][n3 - 1] - dpTable[n1][n2 - 1][n3]
                    # return w(n1, n2, n3 - 1) + w(n1, n2 - 1, n3 - 1) - w(n1, n2 - 1, n3)
                else:
                    dpTable[i][j][k] = dpTable[n1 - 1][n2][n3] + dpTable[n1 - 1][n2 - 1][n3] + dpTable[n1 - 1][n2][n3 - 1] - dpTable[n1 - 1][n2 - 1][n3 - 1]
                    # return w(n1 - 1, n2, n3) + w(n1 - 1, n2 - 1, n3) + w(n1 - 1, n2, n3 - 1) - w(n1 - 1, n2 - 1, n3 - 1)




while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(w(a, b, c))

