'''
작성일 : 2023년 4월 18일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 현재 월을 입력 받아 계절을 출력하시오.
'''
# 1. 월을 입력받는다.
month = int(input("월을 입력하시오 : "))

# 2. 만약 1~12월 사이이면
if month >= 1 and month <= 12 :
    # 1) 만약 3월에서 5월이면
    if 3 <= month <= 5 :
        print("{}월은 봄입니다." .format(month))
    # 2) 만약 6월에서 8월이면
    elif 6 <= month <= 8 :
        print("{}월은 여름입니다." .format(month))
    # 3) 만약 9월에서 11월이면
    elif 9 <= month <= 11 :
        print("{}월은 가을입니다." .format(month))
    # 4) 아니면
    else :
        print("{}월은 겨울입니다." .format(month))
# 3. 아니면
else :
    print("해당 월은 없습니다.")