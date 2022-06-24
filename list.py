# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:45:11 2022

@author: gprua
"""

#리스트와 튜플 응용하기
#append,extend,insert
a=[10,20,30]
a.append(500)#a의 마지막 부분에 500 추가, 요소 하나만 추가 가능
print(a)

a.append([500,1000])#리스트안에 리스트 추가하기
print(a)

a.extend([500,600])#리스트안에 여러가지 요소 추가하기
print(a,len(a))

a.insert(0,500)#특정 위치에 요소 추가하기
print(a)

a.pop()#마지막 요소 삭제
print(a)
a.pop(1)#특정요소 삭제
print(a)

#del도 pop과 똑같은 원리
del a[0]
print (a)

#remove: 특정값을 삭제할 때 사용
a.remove([500,1000])
print(a)

#index:특정값의 인덱스 구하기
print(a.index(500))
print(a.count(500))#count: 특정값의 갯수 구하기
a.reverse()#순서 뒤집기

#정렬하기
a.sort()#오름차순
print(a)
a.sort(reverse=True)#내림차순
print(a)

#삭제및조작
a.clear()
del a[0:]
print(a)