# 11718 그대로 출력하기

import sys

for i in range(100):
    data=list(map(str,sys.stdin.readline()))
    print("".join(data),end='')