# 5622 다이얼

import sys

word_list=list(map(str,sys.stdin.readline()))

ans=0

for i in range(len(word_list)-1):
    if word_list[i]=='A' or word_list[i]=='B' or word_list[i]=='C':
        ans+=3
    elif word_list[i]=='D' or word_list[i]=='E' or word_list[i]=='F':
        ans+=4
    elif word_list[i]=='G' or word_list[i]=='H' or word_list[i]=='I':
        ans+=5
    elif word_list[i]=='J' or word_list[i]=='K' or word_list[i]=='L':
        ans+=6
    elif word_list[i]=='M' or word_list[i]=='N' or word_list[i]=='O':
        ans+=7
    elif word_list[i]=='P' or word_list[i]=='Q' or word_list[i]=='R' or word_list[i]=='S':
        ans+=8
    elif word_list[i]=='T' or word_list[i]=='U' or word_list[i]=='V':
        ans+=9
    else:
        ans+=10
        
print(ans)