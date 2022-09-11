# 4153 직각삼각형

import sys

zero=False

while zero==False:
    length = list(map(int, sys.stdin.readline().split()))
    
    length_sort=sorted(length)
    
    if length==[0,0,0]:
        zero=True
        break
    else:
        if length_sort[2] ** 2 == length_sort[0] ** 2 + length_sort[1] ** 2:
            print("right")
        else:
            print("wrong")