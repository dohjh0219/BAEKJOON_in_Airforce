# 10039 평균 점수

import sys

score_data=[]

for _ in range(5):
    num=int(sys.stdin.readline())
    
    if num<=40:
        num=40
    
    score_data.append(num)
    
print(int(sum(score_data)/5))