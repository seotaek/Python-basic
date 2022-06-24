# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:33:42 2022

@author: gprua
"""

#문자열 응용하기
#문자열 바꾸기
s='Hello,world'
s=s.replace('world','Python')#world를 Python으로 바꿔준다.
print(s)

#문자 바꾸기
table=str.maketrans('eo','12')
print(s.translate(table))#문자열 안의 문자만 바꾸기

#문자열 분리하기
a='a lot of apples,pineapple,model,grape' 
print(a.split(','))#띄어쓰기를 기준으로 문자열을 분리
print('-'.join(a))#join으로 각 문자열 사이에 -들어간다

#잡다
b=' python '
b=b.upper()
print(b)
b=b.lower()#소문자로 변경
print(b)
print(b.lstrip())
print(b.rstrip())
print(b.strip())#공백 없애기 이를 통해 양측의 문자를 없앨수도 있다.

#문자열 위치 찾기
print(b.rfind('th'))#오른쪽에서부터
print(b.index('th'))

c='apple pineapple'
print(c.count('pl'))#문자열 개수 세기

#서식지정자 사용
name='william'
print('I am %s' %name)
x=20
print('%d' % x)
y=2.3
print('%.3f' %y)#소수점아래 3자리 까지 표현

#format메서드
print('Hello,{0} {2} {1}'.format('Python','script',3.6))

#24.5
x=input().split()
count=0
for i in x:
    if(i.strip(',.')=='the'):
        count+=1
print(count)

#24.6
a=list(map(int,input().split(';')))
a.sort(reverse=True)
for i in a:
    print('%9s' % format(i,','))#format 내장함수를 써서 세자리 마다 ,를 찍어준다