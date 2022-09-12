# 1929 소수 구하기

import sys

m,n=map(int,sys.stdin.readline().split())

def isPrime(m,n):
    n=n+1
    prime = [True] * n  # [True]가 n개 있는 리스트 생성
    for i in range(2, int(n**0.5)+1):  # n의 제곱근까지만 검사 실시.
        if prime[i]==True :
            for j in range(2*i,n,i):  # 리스트 내 i의 배수들을 False로 변환.
                prime[j]=False
                
    for i in range(m,n): # 1 이상이면서 남은 소수들을 출력.
        if i>1 and prime[i]==True: 
            print(i)
            
isPrime(m,n)

# 전체적인 흐름은 에라토스테네스의 체를 활용하고 있음. 