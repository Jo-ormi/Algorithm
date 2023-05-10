import sys

n = int(sys.stdin.readline())

bars_stack = []
for i in range(n):
    bars_stack.append(int(sys.stdin.readline()))

max_bar = bars_stack.pop()
cnt = 1

for i in reversed(bars_stack):
  if max_bar < i:
    cnt += 1
    max_bar = i

print(cnt)