# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:03:50 2022

@author: gprua
"""

#값사이에 문자 넣기
print(1,2,sep='+')

print(1,end=' ')
print(2,end=' 3\n')

year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
 
#연습문제7.4
print(year, month, day, sep='/',end=' ')
print(hour, minute, second, sep=':')

#연습문제7.5
year, month, day, hour, minute, second = input().split()

print(year,month,day,sep='-',end='T')
print(hour, minute, second, sep=':')