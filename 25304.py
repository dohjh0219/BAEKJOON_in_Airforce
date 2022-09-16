# 25304 영수증

import sys

x=int(sys.stdin.readline())
n=int(sys.stdin.readline())

sum=0

for i in range(n):
    price,ea=map(int,sys.stdin.readline().split())
    sum+=price*ea
    
if sum==x:
    print("Yes")
else:
    print("No")