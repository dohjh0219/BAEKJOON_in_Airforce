# 2231 분해합

import sys

n=int(sys.stdin.readline())
result=0

for i in range(1,n+1):  # 1에서부터 입력받은 분해합까지 for문 반복.
    num_list=list(map(int,str(i)))  # i를 자리수 별로 리스트화
    result=i+sum(num_list) # result에 분해합 저장
    
    if result == n:  # result에 저장된 분해합 값과 입력받은 n이 같다면,
        print(i) # i를 출력
        break
    
    if i==n:
        print(0)  # 그렇지 않고 결국엔 for문이 입력받은 n값까지 다 돌았음에도 같은 숫자가 나오지 않았다면(생성자가 없다면) 0 출력