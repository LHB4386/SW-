'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 한 과목이 점수를 입력 받아 점수에 따라 학점을 부여하는 프로그램을 작성하시오.
'''
# 1. 점수를 입력받는다.
score = int(input("점수 입력 : "))

# 2. 점수가 90이상이라면
#   1)"A"출력
if score >= 90 and score <= 100 :
    print("A")
    
# 2. 점수가 80이상이라면
#   1)"B"출력
elif score >= 80 and score <= 89 :
    print("B")
    
# 2. 점수가 70이상이라면
#   1)"C"출력
elif score >= 70 and score <= 79 :
    print("C")
    
# 2. 점수가 60이상이라면
#   1)"D학점입니다"출력    
elif score >= 60 and score <= 69 :
    print("D")
    
# 2. 아니면
#   1)"F학점입니다"출력    
else :
    print("F")

    