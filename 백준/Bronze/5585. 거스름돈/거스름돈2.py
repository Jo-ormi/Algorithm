import sys

n = 1000 - int(sys.stdin.read())

change_coin = [500, 100, 50, 10, 5, 1] # 동전의 가치 저장할 리스트 선언
cnt = 0 # 동전의 개수를 저장할 변수
sum_cnt = 0
i = 0 # 동전의 가치 리스트의 인덱스 변수

while n != 0:
  cnt = n//change_coin[i] # 동전의 개수를 저장
  n -= (change_coin[i]*cnt) # 동전의 가치로 나눈 나머지를 저장
  sum_cnt += cnt
  i += 1 # 인덱스를 증가시킨다.
    
print(sum_cnt)
