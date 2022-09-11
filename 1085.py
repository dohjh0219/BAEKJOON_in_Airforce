# 1085 직사각형에서 탈출

import sys

x,y,w,h=map(int,sys.stdin.readline().split())

length_list=[]

length_list.append(x)
length_list.append(w-x)
length_list.append(y)
length_list.append(h-y)

print(min(length_list))