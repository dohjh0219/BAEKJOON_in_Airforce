# 9095 1, 2, 3 더하기

import sys

cache = [0] * 11  # 메모이제이션
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i])

T = int(sys.stdin.readline())

for _ in range(T):
    print(cache[int(sys.stdin.readline())])