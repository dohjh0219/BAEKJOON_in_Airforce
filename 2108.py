# 2108 통계학

import sys

n = int(sys.stdin.readline())

nums = []
for _ in range(n) :
	nums.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(nums)/n))  # nums의 합을 개수로 나눈 값을 반올림.

# 중앙값
nums.sort()  # nums 리스트를 오름차순으로 정렬한 후,
print(nums[int((n-1)/2)])  # 중간의 값을 출력

# 최빈값
counts = dict()  # counts라는 ""딕셔너리"" 생성
for i in range(1,n+1) :
	counts[i] = []  # counts 딕셔너리 안에 빈 자리 생성.

maxCount = 1
count = 1
for j in range(1,n) :
	if nums[j] == nums[j-1] :  # 같은 숫자라면 count에 1 누적.
		count += 1
	else :
		counts[count].append(nums[j-1]) 
		if maxCount < count : maxCount = count
		count = 1
	if j == n-1 : 
		counts[count].append(nums[j])
		if maxCount < count : maxCount = count

if n == 1 :
	counts[1].append(nums[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1 :
	print(counts[maxCount][0])
else :
	print(counts[maxCount][1])

# 범위
print(nums[-1]-nums[0])