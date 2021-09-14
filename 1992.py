N = int(input())
nums = []
for i in range(N):
    nums.append(list(map(int, list(input()))))

answer = ''
def division(n, array):
    global answer 
    if n == 0:
        return
    
    else:
        total = 0
        for arr in array:
            total += sum(arr)
            # print(type(arr))

        if total == (n * n):
            answer += '1'
            return
        elif total == 0:
            answer += '0'
            return
        else:
            answer += '('
            division(n//2, [array[i][:n//2] for i in range(n//2)])
            division(n//2, [array[i][n//2:] for i in range(n//2)])
            division(n//2, [array[(n//2) + i][:n//2] for i in range(n//2)])
            division(n//2, [array[(n//2) + i][n//2:] for i in range(n//2)])
            answer += ')'
            
division(N, nums)
print(answer)