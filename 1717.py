n, m = map(int, input().split())
numList = [i for i in range(n + 1)]


def findRoot(array, number):
    if array[number] != number:
        array[number] = findRoot(array, array[number])
    return array[number]

    # if array[number] == number:
    #     return number
    # return findRood(array, array[number])

def union(array, set1, set2):
    root1 = findRoot(array, set1)
    root2 = findRoot(array, set2)

    if root1 == root2:
        return
    
    array[min(root1, root2)] = max(root1, root2)

for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        union(numList, b, c)
    else: # a == 1
        root1 = findRoot(numList, b)
        root2 = findRoot(numList, c)
        if root1 == root2:
            print("YES")
        else: 
            print("NO")


