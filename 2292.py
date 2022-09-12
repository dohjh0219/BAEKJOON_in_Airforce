# 2292 벌집

import sys
import math

n=int(sys.stdin.readline())

count = 1  # 계차 수열의 an에서 n에 해당하는 숫자임.(위의 입력받은 n과 헷갈리지 않도록 주의.)

while (3*(count**2)-3*count+1)<n:  # 벌집을 원형으로 했을 때 가장 큰 값의 수열은 계차수열임.
    count+=1
    
print(count)