'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 입력 받은 정수가 짝수인지 홀수인지 판단하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다.
num = int(input("정수 입력 : "))

# 2. 만약 입력 받은 정수가 짝수이면 :
#   1)"OO은 짝수입니다."출력
if num % 2 == 0 :
    print("{}은 짝수입니다." .format(num))
    
# 3. 아니면
else :
    print("{}은 홀수입니다" .format(num))