from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 1 :
            
                maps[nx][ny] += maps[x][y]
                q.append((nx,ny))
            
    
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1    