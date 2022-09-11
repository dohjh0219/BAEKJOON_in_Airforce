# 11050 이항 계수 1

import sys
import math

n, k = map(int, sys.stdin.readline().split())

print(int((math.factorial(n))/((math.factorial(k))*math.factorial(n-k))))