def solution(lottos, win_nums):
    answer = []
    z_cnt = 0
    a_cnt = 7
    
    for l in lottos:
        if l == 0:
            z_cnt += 1
        else:
            for w in win_nums:
                if l==w: 
                    a_cnt -= 1
    
    if z_cnt == 0:
        answer.append(6 if(a_cnt>6) else a_cnt) 
        answer.append(6 if(a_cnt>6) else a_cnt) 
    else:
        answer.append(a_cnt - z_cnt) 
        answer.append(6 if(a_cnt>6) else a_cnt) 
        
    return answer