# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:53:33 2022

@author: gprua
"""

#리스트 만들기
person=['james',17,175.3,True]
a=list(range(5,12,2))#(시작점,끝점+1,증가폭)
print(a)#리스트는 변경,추가,삭제불가능 즉,읽기 전용

#튜플 만들기
a=tuple(range(0,10,2))
print(a)
x=map(int,input().split())#문자열 입력방법
a=tuple(x)
print(a)

#10.4
a=list(range(5,-10,-2))
print(a)

#10.5
x=input()
a=tuple(range(-10,10,int(x)))
print(a)