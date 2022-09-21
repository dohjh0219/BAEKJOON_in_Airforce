# 25501 재귀의 귀재

import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global cnt # def 구문 밖에서도 cnt를 사용하기 위해 cnt를 전역변수로 전환시킨다.
    cnt += 1
    
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)  # rstrip은 오른쪽 공백 제거 역할.