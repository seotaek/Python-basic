# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:15:17 2022

@author: gprua
"""

#2차원리스트
a=[[10,20],[30,40],[50,60]]
for i, j in a:
    print(i,j)
for i in a:
    for j in i:
        print(j, end=' ')
    print('')
    
# a=[2,1,3]
# b=[]
# for i in a:
#     line=[]
#     for j in range(i):
#         line.append(int(input()))
#     b.append(line)
# print(b)

import copy
b=copy.deepcopy(a)#2차원 배열을 복사할때는 deepcopy
print(b)

#23.6
a=[[[0 for i in range(3)]for j in range(4)]for k in range(2)]
print(a)