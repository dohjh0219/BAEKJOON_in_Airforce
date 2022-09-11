# 10250 ACM 호텔

import sys

t=int(sys.stdin.readline())

for i in range(t):
    h,w,n = map(int,sys.stdin.readline().split())
    
    
    if n%h==0:
        y=h*100
        x=n//h
    else:
        y=(n%h)*100
        x=1+n//h
    
    print(x+y)