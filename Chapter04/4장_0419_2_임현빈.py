'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 사칙연산의 결과를 출력하는 계산기 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
num1 = int(input("숫자 입력 : "))
cal = input("연산자 입력 : ")
num2 = int(input("숫자 입력 : "))

# 2. 만약 연산자가 + 라면
if cal == '+' :
    print(num1,'+',num2,'=',num1 + num2)
# 1) 아니고 만약 연산자가 - 라면
elif cal == '-' :
    print(num1,'-',num2,'=',num1 - num2)
# 1) 아니고 만약 연산자가 * 라면
elif cal == '*' :
    print(num1,'*',num2,'=',num1 * num2)
# 1) 아니고 만약 연산자가 / 라면
elif cal == '/' :
    print(num1,'/',num2,'=',num1 / num2)

# 3. 아니면
else :
    print("해당 연산자가 없습니다.")