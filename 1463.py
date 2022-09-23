# 1463 1로 만들기

# 전체적인 코드 알고리즘은 다이나믹 알고리즘, 즉 동적계획법을 사용하고 있음.
# 동적계획법의 두 가지 방법 중 바텀업 방식을 이용하고 있다.

import sys

n=int(sys.stdin.readline())
dp=[0]*(n+1)  # 메모이제이션

for i in range(2,n+1):  # for문을 이용하여 2에서부터 n까지의 자연수를 반복한다.
    
    dp[i]=dp[i-1]+1
    
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    
print(dp[n])