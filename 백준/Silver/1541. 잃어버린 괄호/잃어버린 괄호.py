import re

N = input().split("-")

sumlist = []
for n in N:
    numbers = list(map(int,re.findall(r'\d+', n)))
    sumlist.append(sum(numbers))

# print(N)
# print(sumlist)

answer = sumlist[0]
if len(sumlist) > 1:
    for i in range(1,len(sumlist),1):
        answer -= sumlist[i]
else:
    pass

print(answer)