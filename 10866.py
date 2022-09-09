# 10866 덱

from collections import deque
import sys

d = deque()

n = int(sys.stdin.readline())

for i in range(n):
    func=list(map(str,sys.stdin.readline().split()))
    
    if func[0]=='push_front':
        d.appendleft(func[1])
    elif func[0]=='push_back':
        d.append(func[1])
    elif func[0]=='pop_front':
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
    elif func[0]=='pop_back':
        if len(d)==0:
            print('-1')
        else:
            print(d.pop())
    elif func[0]=='size':
        print(len(d))
    elif func[0]=='empty':
        if len(d)==0:
            print('1')
        else:
            print('0')
    elif func[0]=='front':
        if len(d)==0:
            print('-1')
        else: 
            front_num=d.popleft()
            print(front_num)
            d.appendleft(front_num)
    elif func[0]=='back':
        if len(d)==0:
            print('-1')
        else:
            rear_num=d.pop()
            print(rear_num)
            d.append(rear_num)
