def solution(k, m, score):
    answer = 0
    
    score.sort()
    i = 0
    cnt = 0
    for i in range(len(score)-1, -1, -1):   
        cnt += 1
        if (m == cnt):
            answer += score[i] * m 
            cnt = 0
        
    return answer