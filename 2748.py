# 2748 피보나치 수 2

# 전체적인 알고리즘은 동적계획법을 쓰고 있음.


import sys

n=int(sys.stdin.readline())

dp=[0]*(n+1)
dp[1]+=1

def fibo(x):
    for i in range(2,x+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[x]

print(fibo(n))