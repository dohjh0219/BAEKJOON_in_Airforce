# 2775 부녀회장이 될테야

import sys

t=int(sys.stdin.readline())  # test case의 수 입력.

for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    
    f0 = [x for x in range(1,n+1)]  # 0층의 리스트 생성(1,2,3, ...)
    
    for j in range(k):  # k층 수 만큼 반복
        for i in range(1,n):  # i는 인덱스로 사용하는 인자.
            f0[i]=f0[i]+f0[i-1]  # 각 층의 호실 별 사람 수를 더함.
    print(f0[-1])