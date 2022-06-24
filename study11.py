# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:22:44 2022

@author: gprua
"""
#11 시퀀스 자료형
#1.1 특정값이 있는지 확인하기
a=list(range(0,11,2))
print(11 in a)
print(2 in a)

#1.2. 시퀀스 객체 연결하기
a=tuple(range(0,11,2))
b=tuple(range(1,11,2)) #range는 더하기로 연결 불가능 list나 tuple 사용
c=a+b
print(c)

#1.3 시퀀스 객체 반복하기
print(c*3)# *를 활용

#2.1 리스트와 튜플의 요소 개수 구하기
print(len(c))#요소개수를 구하기 위해 len()활용

#2.2 range의 숫자 생성개수 구하기
print(len(range(1,100,7)))

#2.3 문자열의 길이 구하기
i="william seotaek oh"
print(len(i))

#3 인덱스 사용하기
print(i[6])
print(i[-9])#만약 인덱스를 음수로 쓸 경우 뒤에서 부터 출력

i=list(i)  #list로만 삭제가 가능 tuple에서는 불가능
del i[-9]
print(i)

#4 슬라이스 사용하기
a=list(range(0,11,2))
print(a[0:3])#시작지점:자를 지점  자르기 전 지점까지 출력
print(a[ : :2])#인덱스 증가폭
print(a[1:len(a)-1:3])

a[1:3]=[8,9,2,4,6]#고치기
print(a)
del a[1:6]
print(a)

#11.6
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
 
print(year[5:])
print(population[5:])

#11.7
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

#11.8
x=input().split()
del x[-5:]
print(tuple(x))


#11.9
x=input()#split으로 변수를 받으면 안된다.
y=input()
print(x[1:len(x):2]+y[0::2])