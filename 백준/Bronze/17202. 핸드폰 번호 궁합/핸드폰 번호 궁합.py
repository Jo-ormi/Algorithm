import sys

temp = sys.stdin.read()
temp_list = temp.split('\n')
a = temp_list[0]
b = temp_list[1]

a_list = list(a)
b_list = list(b)

couple_list = []

for i in range(len(a)):
  couple_list.append(a[i])
  couple_list.append(b[i])

temp_couple_list = []
while len(couple_list) > 2:
  for i in range(len(couple_list)):
    if i != (len(couple_list)-1):
      temp_couple_list.append((int(couple_list[i])+int(couple_list[i+1]))%10)

    else:
      couple_list = temp_couple_list
      temp_couple_list = []

result = str(couple_list[0]) + str(couple_list[1])
print(result)
