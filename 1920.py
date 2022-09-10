# 1920 수 찾기

from bisect import bisect_left, bisect_right
import sys

n=int(sys.stdin.readline())
a_list=list(map(int, sys.stdin.readline().split()))

m=int(sys.stdin.readline())
search_list=list(map(int,sys.stdin.readline().split()))

a_list.sort()

def count_by_range(a,left_value,right_value):  # count_by_range라는 함수 생성. 이 함수의 인자인 left_value와 right_value 사이에 존재하는 숫자의 갯수를 반환하는 함수.
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

for i in range(m):
    if count_by_range(a_list, search_list[i],search_list[i])==0:  # count_by_range 함수에서 left_value와 right_value 인자가 같으므로 그 숫자의 갯수를 셀 수 있게 된다.
        print('0')
    else:
        print('1')
    