# 11866 요세푸스 문제 0

n,k = map(int,input().split())

data=[i for i in range(1,n+1)]   # 1부터 n까지의 자연수 리스트 생성.

josephus=[]  # 제거될 자연수 저장 리스트(요세푸스 순열)
num=0  # 제거될 자연수의 위치 인덱스

for i in range(n):
    num += k-1;
    if num>=len(data):  #원을 한바퀴 모두 돌아버린 경우.
        num = num % len(data)
        
    josephus.append(str(data.pop(num)))  # pop기능을 통해 index가 num인 데이터를 끄집어낸다. 이 데이터는 str을 통해 문자열 형태로 반환. 
    
    
print("<",", ".join(josephus)[:],">", sep='')  # join 함수는 문자열을 일정하게 합쳐주는 기능. ".join(리스트)  -> 이와 같은 형태로 사용.