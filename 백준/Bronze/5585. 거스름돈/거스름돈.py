import sys

target = 1000 - int(sys.stdin.readline())

a = target // 500
target -= (500*a)


b = target // 100
target -= (100*b)

c = target // 50
target -= (50*c)

d = target // 10
target -= (10*d)

e = target // 5
target -= (5*e)

f = target


print(a+b+c+d+e+f)