'''
작성일 : 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395029
이름 : 임현빈
설명 : 7장 세트와 딕셔너리
      02. 딕셔너리
      
키(key)와 값(value)을 한 요소로 묶어 표현한 자료구조
키는 중복을 허용하지 않음
세트처럼 순서가 없는 자료형
각 요소에서 키와 같은 ":"으로 구분
'''
# 딕셔너리 생성
dict1 = {1:'one', 2:'two', 3:'three'}
print("딕셔너리 dict1 내용 : ", dict1)

# 리스트를 딕셔너리로 변환
list1 = [[1,'하나'], [2,'둘'], [3,'셋']]
dict2 = dict(list1)
print("리스트 list1 내용 : ", list1)
print("딕셔너리 dict2 내용 : ", dict2)

# 키(key)를 지정하여 값(value) 검색
print("딕셔너리 dict2의 키 3의 값 : ", dict2.get(3))

# 딕셔너리 모든 요소 삭제
dict2.clear()
print("딕셔너리 dict2 내용 : ", dict2)

# keys() 메소드 이용하여 사전의 모든 키 출력
print("dict1의 key : ", end=' ')
# 반복문 사용하여 키 출력
for num in dict1.keys() :
    print(num, end=', ')
print()

# values() 메소드 이용하여 사전의 모든 값 출력
for alpanum in dict1.values() :
    print(alpanum, end=', ')
print()

# items() 메소드 이용하여 사전의 모든 키와 값 출력
for num, alpanum in dict1.items() :
    print(num,"은(는) 영어로", alpanum)