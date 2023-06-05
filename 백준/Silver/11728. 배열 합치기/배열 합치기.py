import sys

cnt_list = list(map(int, sys.stdin.readline().split(" ")))
frist_cnt = cnt_list[0]
second_cnt = cnt_list[1]


arr1 = list(map(int, sys.stdin.readline().split(" ")))
arr2 = list(map(int, sys.stdin.readline().split(" ")))

for i in range(second_cnt):
    arr1.append(arr2[i])

arr1.sort()

for a in arr1:
    print(a, end=" ")


