# 2164 카드2 

from collections import deque
import sys

d = deque()

n = int(sys.stdin.readline())

for i in range(1,n+1):
    d.append(i)   # 1에서 n까지의 자연수들을 데크에 저장.
    
while len(d)!=1:  # 데크의 데이터가 하나가 될 때 까지 while 반복문 실행.
    d.popleft();  # 가장 위에 있는 카드 제거
    d.rotate(-1); # 원형 데크를 -1만큼(반대로 회전시켜 맨 위의 카드를 맨 뒤로 보냄.)
    
print(d.pop()) # 하나 밖에 남지 않은 카드 출력.