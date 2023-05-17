 # 백준 9095번
import sys

def calList(n):

  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return calList(n-1) + calList(n-2) + calList(n-3)



N = int(sys.stdin.readline())
for i in range(N):
    cnt = 0
    cnt += calList(int(sys.stdin.readline()))
    print(cnt, end=' ')
  


  
