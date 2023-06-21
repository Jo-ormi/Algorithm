import random

N = int(input())

cnt = 0

while N:
    pick = random.choice([1, 3])
    
    if N - pick < 0:
        pick = 1
    
    N -= pick
    
    cnt += 1

if(cnt % 2 == 0):
    print("CY")
else:
    print("SK")