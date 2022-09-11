# 1966 프린터 큐

from collections import deque
import sys

n=int(sys.stdin.readline())

for i in range(n):
    n,m=map(int,sys.stdin.readline().split())
    queue=deque(list(map(int,sys.stdin.readline().split())))
    count = 0
    
    while queue:
        high_level=max(queue)  # 중요도가 최대인 값이 가장 먼저 배출되므로 최댓값 저장.
        front=queue.popleft() 
        m=m-1
        
        if high_level==front:
            count=count+1
            if m<0:
                print(count)
                break
        else:
            queue.append(front)
            if m<0:
                m=len(queue)-1