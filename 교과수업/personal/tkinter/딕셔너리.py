
dic={'학반':105,'번호':20,'이름':'홍길동','연락처':'010-1111-2222'}
print(dic)
dic['연락처']='010-1111-2223' #2222->2223
print(dic)

#키로 값 찾기
print(dic['학반'])
print(dic['번호'])
print(dic['이름'])

#키로 값에 접근
print(dic.get('이름'))

#차이점
print(dic.get('주소'))#반환값-none
#print(dic['주소']) #에러

#딕셔너리의 모든 키 반환
print(dic.keys())
print(list(dic.keys()))#키값을 리스트화

#딕셔너리의 모든 값 반환
print(dic.values())
print(list(dic.values()))

#딕셔너리 안에 키가 있는지 확인(출력은 불 자료형으로 출력)
print('이름' in dic)
print('주소' in dic)