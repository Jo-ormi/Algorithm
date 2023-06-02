def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    box = []
    i = 0
    for i in range(0, len(score), i+m):   
        if (i+m > len(score)):
            break
        box.append(score[i:i+m])
    
    for b in box:
        answer += b[-1] * m 
        
    return answer