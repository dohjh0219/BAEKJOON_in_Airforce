# 1259 팰린드롬수

import sys

zero=False

while zero==False:
    num=int(sys.stdin.readline())
    
    if num==0:
        zero=True
        break
    else:
        num_list=list(map(int,str(num)))
        rev_num=list(reversed(num_list))
        if num_list==rev_num:
            print("yes")
        else:
            print("no")