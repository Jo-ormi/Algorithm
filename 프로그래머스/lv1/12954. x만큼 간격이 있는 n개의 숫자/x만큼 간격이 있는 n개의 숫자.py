def solution(x, n):
    answer = [0 for i in range(n)]
    
    for i in range(0,n):
        answer[i] = x * (i+1)
    
    return answer