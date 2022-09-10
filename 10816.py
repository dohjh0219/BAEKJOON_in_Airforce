# 10816 숫자 카드 2

from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline())  # 상근이가 갖고 있는 숫자 카드의 갯수 N 입력
card_data=list(map(int, sys.stdin.readline().split()))  # 숫자카드에 적혀있는 정수 입력.
m = int(sys.stdin.readline())  # 탐색하는 숫자의 개수 M 입력.
search_data=list(map(int, sys.stdin.readline().split()))  # 탐색 할 숫자 입력.

card_data.sort()

def count_by_range(a,left_value,right_value):  # count_by_range라는 함수 생성. 이 함수의 인자인 left_value와 right_value 사이에 존재하는 숫자의 갯수를 반환하는 함수.
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

for i in range(len(search_data)):
    print(count_by_range(card_data, search_data[i],search_data[i]),end=' ')  # count_by_range 함수에서 left_value와 right_value 인자가 같으므로 그 숫자의 갯수를 셀 수 있게 된다.