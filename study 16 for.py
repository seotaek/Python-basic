# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:28:05 2022

@author: gprua
"""

#반복문
for i in range(100):
    print('Hello world')
    
count=int(input())
for i in range(count):
    print(i)
    
for letter in reversed('python'):#letter이란 변수에 뒤집힌python을 집어넣는다고 생각
    print(letter)
    
#16.5
x = [49, -17, 25, 102, 8, 62, 21]

for i in range(7):
    print(x[i]*10, end=' ')
    
#16.6
x=int(input())

for i in range(1,10,1):
    print('{} * {} = {}'.format(x,i,x*i))
    #print(n, '*', i, '=', n*i)