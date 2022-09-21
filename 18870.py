# 18870 좌표 압축

import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr2 = list(sorted(set(arr)))  # arr2 리스트에는 arr에서 중복을 제거하고 난 후 오름차순 정렬한 데이터를 저장.

dic = {arr2[i]:i for i in range (len(arr2))} # dic에는 해당숫자:개수 형태로 저장함.

for i in arr: # arr 순서대로(정렬되기 전) 출력
    print(dic[i],end=' ') 