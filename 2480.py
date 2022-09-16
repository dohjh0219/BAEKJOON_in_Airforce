# 2480 주사위 세개

import sys

a,b,c = map(int,sys.stdin.readline().split())
search_max=[]
search_max.append(a)
search_max.append(b)
search_max.append(c)


if a==b or b==c or c==a :
    if a==b==c:
        print(10000+a*1000)
    else:
        if a==b:
            print(1000+a*100)
        elif b==c:
            print(1000+b*100)
        else:
            print(1000+c*100)
            
else:
    print(max(search_max)*100)