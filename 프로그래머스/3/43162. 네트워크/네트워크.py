from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    
    def BFS(i):
        q.append(i)
        
        while q:
            ni = q.popleft()
            
            visited[ni] = 1
            
            for j in range(n):
                if not visited[j] and computers[ni][j] == 1:
                    q.append(j)
        
    visited = [0 for _ in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            
    
    
    return answer