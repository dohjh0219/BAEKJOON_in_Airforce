# 10870 피보나치 수 5

import sys

n=int(sys.stdin.readline())

fibo=[0,1]

if n>=2:
    for i in range(n-1):
        fibo.append(fibo[i]+fibo[i+1])

print(fibo[n])