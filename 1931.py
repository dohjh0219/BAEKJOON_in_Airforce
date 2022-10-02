# 1931 회의실 배정

import sys

n = int(sys.stdin.readline())
room = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    room.append([a, b])

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)