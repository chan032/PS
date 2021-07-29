from collections import deque 

def solution(bLen, w, wList):
    answer = 0
    ingList = deque([0] * bLen)
    wList = deque(wList)
    
    
    totalSum = 0
    while True:
        if not wList:
            answer += bLen 
            break
            
            
        answer += 1
        # totalSum을 sum함수로 처리할 경우 시간초과 발생
        # 삽입 가능
        if (totalSum - ingList[0] + wList[0]) <= w:
            t = wList.popleft()
            totalSum -= ingList.popleft()
            ingList.append(t)
            totalSum += t
        # 삽입 불가능
        else:
            totalSum -= ingList.popleft()
            ingList.append(0)
            
    return answer