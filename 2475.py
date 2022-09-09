# 2475 검증수

a,b,c,d,e = map(int, input().split())  ##고유번호 5자리 입력.

verify_num=(a*a+b*b+c*c+d*d+e*e)%10

print(verify_num)