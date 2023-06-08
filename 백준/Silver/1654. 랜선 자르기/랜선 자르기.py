import sys

cnt_list = list(map(int, sys.stdin.readline().split()))
my_cnt = cnt_list[0]
want_cnt = cnt_list[1]

my_list = []
min_length = 0
max_length = 0
for i in range(my_cnt):
    new_length = int(sys.stdin.readline())
    my_list.append(new_length)
    if new_length > max_length:
        max_length = new_length

max_length+=1
while(min_length < max_length):
    mid = (min_length + max_length) // 2

    cnt = 0

    for m in my_list:
        cnt += m//mid

    if(cnt < want_cnt):
        max_length = mid
    else:
        min_length = mid+1

print(min_length-1)