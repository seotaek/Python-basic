# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:42:10 2022

@author: gprua
"""

#Fizz buzz
x=int(input())
for i in range(1,x):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
        
for i in range(1,x):
    print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)
    
#20.7
for i in range(1, 101):
    if i%2==0 and i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)
        
#20.8
x,y=map(int,input().split())
for i in range(x,y+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)