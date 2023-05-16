import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))


N_list_dict = dict()
for n in N_list:
    if n in N_list_dict:
        N_list_dict[n] += 1
    else:
        N_list_dict[n] = 1

for m in M_list:
    if m in N_list_dict:
        print(N_list_dict[m], end=' ')    # 존재하는 숫자 카드라면
    else:
        print(0, end=' ')    