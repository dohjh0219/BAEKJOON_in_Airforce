# 9020 골드바흐의 추측(시간초과 오답 코드. 답은 맞으나 시간초과 해결 필요.)

import sys
import math

n=int(sys.stdin.readline())

def num(num): # 소수 구하는 함수
    if num == 1:  # 1은 소수가 아니므로 False 반환
        return False
    else :
        for i in range(2,int(math.sqrt(num))+1) : # sqrt는 제곱근 기능임. 
            if num%i == 0: # num이 i에 의해서 나누어 떨어지면 소수가 아니라는 의미이므로 False 반환. 
                return False
        return True

all_list = list(range(2,10000)) # 문제에서 주어진 범위 리스트 생성.
save_list=[]


for i in all_list : # all_list에 있는 범위 만큼 소수 검색.
    if num(i):
        save_list.append(i) # 소수라면 save_list에 append. 즉 save_list에는 범위 내 소수가 모두 저장됨.and
        
result=[]
cha=[]

for i in range(n):
    num=int(sys.stdin.readline())
    result.clear()
    cha.clear()
    
    for j in save_list:
        if num-j>=0:
            if save_list.count(num-j)>0:  # num에 대응하는 값이 소수 리스트에 있는가?
                result.append([j,num-j])
            else:
                continue
    
    if len(result)>0:
        for k in range(len(result)):
            cha.append((result[k][0]-result[k][1])**2)
        print(result[cha.index(min(cha))][0],result[cha.index(min(cha))][1],sep=' ')
    else:
        print(0,num,sep=' ')