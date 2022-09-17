# 1712 손익분기점

import sys

a,b,c = map(int,sys.stdin.readline().split())

if c<=b: # c<=b라면 손익분기점이 발생하지 않음.
    print(-1)
else:
    print(a//(c-b)+1)  # 손익분기점 계산식의 몫 값(정수값)만 출력 시킴.
    # 위의 식에서 더하기 1을 한 이유는 해당 몫 값은 손익분기점 바로 전 값이므로 하나 더 커야 그게 손익분기점이 되기 때문이다.