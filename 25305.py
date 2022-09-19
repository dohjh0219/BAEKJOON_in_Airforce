# 25305 커트라인

import sys

n,k=map(int,sys.stdin.readline().split())
score=list(map(int,sys.stdin.readline().split()))
sort_score=sorted(score, reverse=True)
print(sort_score[k-1])