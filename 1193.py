# 1193 분수찾기

import sys

x = int(sys.stdin.readline())
num_list = []

num = 0
num_count = 0

while num_count < x:  # 등차수열 계속해줌. num에 몇 번째 그룹인지 저장됨.
    num += 1
    num_count += num

num_count -= num  # num_count에는 x가 포함된 그룹의 바로 전 그룹의 마지막 숫자가 몇 번째인지 저장됨.

if num % 2 == 0: # 짝수 번째 그룹이라면, 
    i = x - num_count
    j = num - i + 1
else: # 홀수 번째 그룹이라면, 
    i = num - (x - num_count) + 1 
    j = x - num_count

print(f"{i}/{j}")
