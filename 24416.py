# 24416 알고리즘 수업 - 피보나치 수 1
# 미완성

import sys

x=int(sys.stdin.readline())

count1=0
count2=0

def fib(n):
    global count1
    if n==1 or n==2:
        return 1
    else:
        count1+=1
        return fib(n-1)+fib(n-2)
    

def fibonacci(n):
    global count2
    
    dp=[0]*(n+1)   # 메모이제이션
    dp[1]=1
    dp[2]=1
    
    for i in range(3,n+1):
        count2+=1
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[n]

num1=fib(x)
num2=fibonacci(x)

print(count1+1, count2, sep=' ')