# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

ea=list(map(int,sys.stdin.readline().split()))

need_ea=[0 for i in range(6)]

need_ea[0]=1-ea[0]
need_ea[1]=1-ea[1]
need_ea[2]=2-ea[2]
need_ea[3]=2-ea[3]
need_ea[4]=2-ea[4]
need_ea[5]=8-ea[5]

print(' '.join(str(x) for x in need_ea))
# 리스트를 공백으로 구분하여 출력하는 방법