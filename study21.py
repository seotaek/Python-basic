# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:54:46 2022

@author: gprua
"""

#사각형그리기
import turtle as t
t.shape('turtle')

for i in range(4):
     t.forward(100) #입력한 숫자만큼 앞으로 이동
     t.right(90) #입력한 숫자의 각도 만큼 꺾음
    
#다각형
x=int(input())
t.color('green')
t.begin_fill()
for i in range(x):
     t.forward(100) #입력한 숫자만큼 앞으로 이동
     t.right(360/x) #입력한 숫자의 각도 만큼 꺾음
t.end_fill()

#원그리기
t.circle(120)#반지름의 길이 120인 원

n=int(input())
t.speed('fastest')
for i in range(n):
    t.circle(120)
    t.right(360/n)
    
#21.5 오각별 그리기
n=5
for i in range(5):
    t.forward(100)
    t.right(144)#외각 기중
    t.forward(100)
    t.left(72)
    
#21.6 
n, line = map(int, input().split())
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)