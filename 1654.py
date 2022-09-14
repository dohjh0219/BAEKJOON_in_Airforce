# 1654 랜선 자르기

import sys

k,n=map(int,sys.stdin.readline().split())  # k는 이미 갖고 있는 선의 개수, n은 나눠야 하는 목표 개수
arr=[]

for i in range(k):
    arr.append(int(sys.stdin.readline()))  # 각 랜선의 길이를 입력받아 arr에 저장.
    
start = 1
end = max(arr)

while(start<=end):  # 이진탐색 알고리즘을 이용함.
    mid=(start+end)//2  # 몫 연산자를 통해 중간값 구함.
    cnt=0
    
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n :
        start=mid+1
    else:
        end=mid-1
        
print(end)

