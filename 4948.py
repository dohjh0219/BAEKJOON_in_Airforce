# 4948 베르트랑 공준

import math
import sys

def num(num): # 소수 구하는 함수
    if num == 1:  # 1은 소수가 아니므로 False 반환
        return False
    else :
        for i in range(2,int(math.sqrt(num))+1) : # sqrt는 제곱근 기능임. 
            if num%i == 0: # num이 i에 의해서 나누어 떨어지면 소수가 아니라는 의미이므로 False 반환. 
                return False
        return True

all_list = list(range(2,246912)) # 문제에서 주어진 범위 리스트 생성.
save_list=[]

for i in all_list : # all_list에 있는 범위 만큼 소수 검색.
    if num(i):
        save_list.append(i) # 소수라면 save_list에 append. 즉 save_list에는 범위 내 소수가 모두 저장됨.


num = int(sys.stdin.readline())

while num != 0:
    count = 0
    for i in save_list: # 저장된 소수들 중,
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())