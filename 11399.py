# 11399 ATM

import sys

n=int(sys.stdin.readline())
time=list(map(int,sys.stdin.readline().split()))

def greedy(x,t):
    over_time=[]
    complete_time=0
    
    for _ in range(len(t)):
        over_time.append(min(t))
        t.remove(min(t))
        complete_time+=sum(over_time)
        
    return complete_time

print(greedy(n,time))