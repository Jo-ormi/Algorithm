import sys

target = sys.stdin.read()
alphabet = [0] * 27

for n in target:
    if n.islower():
      alphabet[ord(n) % 97] += 1

max_alphabet = max(alphabet)
for i in range(len(alphabet)):
  if max_alphabet == alphabet[i]:
    print(chr(i+97), end='')
