# 11047 동전 0

import sys

n,k=map(int,sys.stdin.readline().split())
coin_type=[]

for _ in range(n):
    coin_type.append(int(sys.stdin.readline()))
    
def greedy(coin,target):
    coin.sort(reverse=True)
    count=0
    
    while target!=0:
        for i in coin:
            if i<=target:
                count+=target//i
                target-=i*(target//i)
    
    return count

print(greedy(coin_type,k))