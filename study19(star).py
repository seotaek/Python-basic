# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:13:32 2022

@author: gprua
"""

#별찍기
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*',end='')#end로 줄이 바뀌지 않게 설정
    print()
    
#대각선으로 찍기
for i in range(5):
    for j in range(5):
        if j==i:
            print('*',end='')#end로 줄이 바뀌지 않게 설정
        else:
            print(' ',end='')
    print()
    
#19.5
for i in range(5):
    for j in range(5):
        if i<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
#19.6
count=int(input())
for i in range(count):
    for j in reversed(range(count)):
        if i<j:
            print(' ',end='')
        else:
            print('*',end='')
    for j in range(count):
        if i>j:
            print('*',end='')
    print()