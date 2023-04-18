'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 한 과목이 점수를 입력 받아 점수에 따라 학점을 부여하는 프로그램을 작성하시오.
'''
# 1. 점수를 입력받는다.
score = int(input("점수 입력 : "))

# 2. 만약 점수가 0~100 사이라면
if score >= 0 and score <= 100 :
    # 1) 만약 점수가 90점 이상이면
    if score >= 90 :
        print("{}점은 A학점" .format(score))
    # 2) 아니고 만약 점수가 80점 이상이면
    elif score >= 80 :
        print("{}점은 B학점" .format(score))
    # 3) 아니고 만약 점수가 70점 이상이면
    elif score >= 70 :
        print("{}점은 C학점" .format(score))
    # 4) 아니고 만약 점수가 60점 이상이면
    elif score >= 60 :
        print("{}점은 D학점" .format(score))
    # 5) 아니면
    else :
        print("{}점은 F학점" .format(score))
# 3. 아니면
else :
    print("잘못입력된 점수입니다.")