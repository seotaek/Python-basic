# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 22:11:53 2022

@author: gprua
"""

#while문
import random

i=0
while i !=3:
    i=random.randint(1,10)
    print (i)
    
#17.5
i=2
j=5

while j>0 or i<=32:
    print(i,j)
    i*=2
    j-=1
    
#17.6
price=int(input())

while price>=1350:
    price-=1350
    print(price)
    
#18.5
i = 0
while True:
   if i%10!=3:
       i+=1
       continue
   if i>73:
       break
   
   print(i, end=' ')
   i += 1
   
#18.6
start, stop = map(int, input().split())
 
i = start
 
while True:
    if i<=stop:
        if i%10==3:
            i+=1
            continue
    else:
        break
    print(i, end=' ')
    i += 1