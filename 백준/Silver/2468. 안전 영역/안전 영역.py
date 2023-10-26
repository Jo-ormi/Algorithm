# 백준 2468

# 이하

from collections import deque
import copy
n = int(input())

maps = []
maxs = []
for i in range(n):
    temp = list(map(int, input().split(' ')))
    maxs.append(max(temp))
    maps.append(temp)

# print(maps)
max_num = max(maxs)
q = deque()

def bfs(temp_maps, i,j):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    q.append((i,j))
    temp_maps[i][j] = 0

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if nx>=0 and ny>=0 and nx<n and ny<n and temp_maps[nx][ny]==1:
                temp_maps[nx][ny] = 0
                q.append((nx,ny))

    return 0
  

answer = []
for mn in range(max_num):
    temp_maps = copy.deepcopy(maps)
    count = 0
    for i in range(n):
        for j in range(n):
          if temp_maps[i][j] <= mn:
            temp_maps[i][j] = 0
          else:
            temp_maps[i][j] = 1

      # print(temp_maps)
    for i in range(n):
        for j in range(n):
          if temp_maps[i][j] == 1:
            bfs(temp_maps, i,j)
            count += 1
    answer.append(count)

# print(answer)
print(max(answer))
