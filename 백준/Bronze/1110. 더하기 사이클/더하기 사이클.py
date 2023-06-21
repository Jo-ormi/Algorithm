#백준 더하기 사이클 1110번
N = input()

count = 0
answer = int(N)

while True:
    if int(N) < 10:
        N = '0' + N
        
    temp = str(int(N[0]) + int(N[-1]))
    
    N = N[-1] + temp[-1]
    count += 1
    
    if answer == int(N):
        break

print(count)