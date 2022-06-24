# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:59:31 2022

@author: gprua
"""

#13조건문
x=int(input())


if x==10:
    print('x에 들어있는 숫자는')
    print('10입니다.')#들여쓰기가 매우 중요하다
    
#중첩 조건문
if x>=10:
    print('10이상')
    
    if x==15:
        print('15입니다')
    if x==20:
        print('20입니다')
        
#13.6
x=5

if x!=10:
    print('ok')
    
#13.7
price=int(input())
coupon=input()

if(coupon=='Cash3000'):
    print(price-3000)
if(coupon=='Cash5000'):
    print(price-5000)
    
if not '':#빈문자열은 false로 출력
    print(True)
else:
    print(False)
    
#14.6
written_test = 75
coding_test = True
 
if written_test>=10 and coding_test=='True':
    print('합격')
else:
    print('불합격')
    
#14.7
a,b,c,d=map(int,input().split())
y=a+b+c+d
    
avg=y/4


if(0<=a<=100 and 0<=b<=100 and 0<=c<=100 and 0<=d<=100):
    if(avg>=80):
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
    
#15.3
x=int(input())

if 11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')
    
#15.4
age=int(input())
balance=9000

if(7<=age<=12):
    balance-=650
elif(13<=age<=18):
    balance-=1050
elif(age>=19):
    balance-=1250
    
print(balance)
