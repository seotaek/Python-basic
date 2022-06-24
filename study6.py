# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:40:18 2022

@author: gprua
"""

x,y,z=10,20,30#변수 한번에 만들기
print(x,y,z)
x,y,z=y,z,x#변수 값 한번에 바꾸기
print(x,y,z)
x=None#빈변수 생성
print(x,y,z)

d=y
d+=10#산술 연산을 하기 위해서는 변수에 값이 할당되어 있어야한다.
print(d)

#입력 값을 변수에 저장하기
x=input("숫자를 입력하세요:")
print(x)
y=input("숫자를 입력하세요:")
print(x+y)#x+y가 아닌x와y가 이어져서 나온다 input으로 받을경우 문자열로 받기 때문에
#따라서 정수나 실수로 변환후 연산이 필요
x=int(x)
y=int(y)
print(x+y)

#입력 값을 변수 2개에 저장하기
#a,b=input('숫자 두개를 입력하세요:').split()#입력받은 값을 공백을 기준으로 분리
#a,b=int(a),float(b)
#print(a+b)

#map을 사용하여 정수로 변환하기
a,b=map(int,input('숫자 2개를 입력하세요:').split(','))#입력받은 값을 , 기준으로 분리
print(a+b)

#연습문제6.6
p,q,r=map(int,input().split())
print(p+q+r)

#심사문제6.7
a=50
b=100
c=None
print(a)
print(b)
print(c)

#심사문제6.8
a,b,c,d=map(int,input().split())
x=(a+b+c+d)//4
print(x)