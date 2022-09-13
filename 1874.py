# 1874 스택 수열

# 뭐가 뭔지 하나도 모르겠음.

import sys

count=1
temp=True
stack=[]
op=[]

n=int(sys.stdin.readline())

for i in range(n):
    n=int(sys.stdin.readline())
    
    while count <= n:
        stack.append(count)
        op.append('+')
        count += 1
    
    if stack[-1]==n:
        stack.pop()
        op.append('-')
    else:
        temp=False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)