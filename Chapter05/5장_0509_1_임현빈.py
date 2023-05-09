'''
작성일 : 2023년 5월 09일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 정수를 입력 받아 입력 받은 수가 소수인지 아닌지 판단하는 프로그램을 작성하시오.
'''
# 1. 정수를 입력받는다.
# 2. 1부터 입력 받은 수까지 반복하면서
#   1) 만약 수를 입력 받은 수로 나누어 나머지가 0이면
#   멈춘다.
# 3. 만약 입력 받은 수와 나누는 수가 같으면
#   1) oo은 소수입니다.
# 4. 아니면
#   1) oo은 소수가 아닙니다.

input_num = int(input("정수를 입력하시오 : "))

for num in range(2, input_num + 1) :
    if input_num % num == 0 :
        break
if input_num == num :
    print("{}은 소수입니다." .format(input_num))
else :
    print("{}은 소수가 아닙니다." .format(input_num))
    
print("==============================")

input_num = int(input("정수를 입력하시오 : "))
count = 0
for num in range(2, input_num + 1) :
    if input_num % num == 0 :
            count = count + 1
if count == 1 :
    print("{}은 소수입니다." .format(input_num))
else :
    print("{}은 소수가 아닙니다." .format(input_num))
