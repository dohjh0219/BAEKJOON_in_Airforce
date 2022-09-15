# 2525 오븐 시계

import sys

h,m=map(int,sys.stdin.readline().split())

time=int(sys.stdin.readline())

state=False

m+=time
while state==False:
    
    
    if m>=60:
        h+=1
        m-=60
    else:
        if h>=24:
        	h-=24
        else:
        	state=True
    
print(h,m,sep=' ')