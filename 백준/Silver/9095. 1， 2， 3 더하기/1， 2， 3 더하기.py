import sys

def calList(list_len):

  if list_len == 1:
    return 1
  elif list_len == 2:
    return 2
  elif list_len == 3:
    return 4
  else:
    return calList(list_len-1) + calList(list_len-2) + calList(list_len-3)



N = int(sys.stdin.readline())
for i in range(N):
    basic_list = [1] * int(sys.stdin.readline())
    cnt = 0
    
    cnt += calList(len(basic_list))
    print(cnt, end=' ')
