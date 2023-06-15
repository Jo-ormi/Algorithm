# 백준 1260번
from collections import deque

init_list = list(map(int, input().split(" ")))
N = init_list[0]
dfs_list = [False for i in range(N+1)]
bfs_list = [False for i in range(N+1)]

M = init_list[1]
V = init_list[2]

node_list = [[] for i in range(N+1)]
for i in range(M):
    temp_list = []
    temp_list = list(map(int, input().split(" ")))

    node_list[temp_list[0]].append(temp_list[1])
    node_list[temp_list[1]].append(temp_list[0])

for i in range(N+1):
    node_list[i].sort()


def DFS(node_list, V, dfs_list):
    # 현재 노드를 방문 처리
    dfs_list[V] = True
    print(V, end = ' ')

    for i in node_list[V]:
        if not dfs_list[i]:
            DFS(node_list, i, dfs_list)

  
def BFS(node_list, V, bfs_list):
    queue = deque([V])
    # 현재 노드를 방문 처리
    bfs_list[V] = True
    while queue:
        b = queue.popleft();
        print(b, end = ' ')

        for i in node_list[b]: # 여기다 여기야
          if not bfs_list[i]:
            queue.append(i)
            bfs_list[i] = True

DFS(node_list, V, dfs_list)
print()
BFS(node_list, V, bfs_list)