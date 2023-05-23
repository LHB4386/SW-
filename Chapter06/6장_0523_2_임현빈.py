'''
작성일 : 2023년 5월 23일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 6장 시퀀스 자료형
       05. 다중 리스트
'''
# 다중 리스트
num =[[11,12,13], [21,22,23], [31,32,33,34], [41,42]]

# 리스트 내의 각각 리스트의 합계를 계산하여 출력
for i in range(len(num)) :  # num 리스트의 길이만큼 반복
    total = 0
    for j in range(len(num[i])) :  # 0번지의 길이까지 반복
        total = total + num[i][j]
    print(i+1, "번째 줄의 합 :", total)

# 실습 예제 6-5
# 1~100 사이의 랜덤 수를 발생시켜 리스트에 저장하고,
# 합계, 최대값, 최소값을 출력하시오.
# 오름차순으로 정렬도 하시오.
import random   # 랜덤 함수를 포함
num = []    # 빈 리스트 생성

for i in range(10) :
    num.append(random.randint(1,100))
    
print("생성된 리스트 : ", num)
print("합계 : ", sum(num))
print("최댓값 : ", max(num))
print("최소값 : ", min(num))
num.sort()  # 정렬 후에 출력하기
print("정렬된 리스트 : ", num)
