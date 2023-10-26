#백준 2667 단지 번호 붙이기

from collections import deque

n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(int, list(input()))))
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]


q = deque()

visited = [[0] * n for _ in range(n)]

answer = []

def bfs(a,b):
    q.append((a,b))
    cnt = 1

    visited[a][b] = 1

    while q:
        x, y = q.popleft()
      
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
          
            if nx >= 0 and ny >=0 and nx < n and ny < n:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1

    return cnt

    
for i in range(n):
  for j in range(n):
    if not visited[i][j] and maps[i][j] == 1:
        total = bfs(i,j)
        answer.append(total)
    
        
print(len(answer))
answer.sort()
for a in answer:
    print(a)
        
     
            
      