'''
작성일 : 2023년 4월 5일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 사용자로부터 평점을 입력 받아 평점을 출력하고,
       입력된 평점이 4.2 이상이면
       "해외 연수 기회 부여"를 출력하는 프로그램을 작성하시오.
'''
# 1. 평점을 입력받아 실수형으로 변환하여 변수 score에 저장한다.
score = float(input("평점을 입력하시오(예:4.5) : "))

# 2. 입력받은 평점을 출력한다.
print("당신의 평점은 : ", score,"입니다.")
print("당신의 평점은 : {}입니다." .format(score))

# 3. 만약 입력받은 평점이 4.2 이상이면
#     3-1. "해외 연수 기회 부여"를 출력한다.
if score >= 4.2 :
    print("해외 연수 기회 부여")

# 4. "감사합니다"를 출력한다.
print("감사합니다.")
    