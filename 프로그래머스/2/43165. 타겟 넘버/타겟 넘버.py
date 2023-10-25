
def solution(numbers, target):
    
    whole_sum = [0]
    
    answer = 0

    for n in numbers:
        temp = []
        for w in whole_sum:
            temp.append(w+n)
            temp.append(w-n)
        whole_sum = temp
    
    for w in whole_sum:
        if w == target:
            answer += 1
            
    return answer
   