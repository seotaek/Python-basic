# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:42:35 2022

@author: gprua
"""

#리스트의 할당과 복사

a=[0,0,0,0,0]
b=a#뒤에 어떻게 바뀌든 b와a가 똑같아 진다
b[2]=99
print(a)
c=a.copy()
print(c)

#반복문으로 리스트의 요소를 모두 출력하기
a=[38,21,53,62,19]
for i in a:
    print(i)
    
#index와 값 같이 출력하기    
for index, value in enumerate(a):
    print(index,value)
    
#최대값,최소값 구하기
print(min(a),max(a))
#합계
print(sum(a))

#특이한 list 생성방법
c=[i+5 for i in range(10)]#0부터 9까지 5를 더한 list
print(c)

d=[i for i in range(10) if i%2==0]
print(d)#짝수만 출력


#list에서 map사용하기
x=list(map(int,input().split()))
print(x)

#22.9
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b=[i for i in a if len(i)==5]
print(b)

#22.10
x,y=map(int,input().split())
a=[2**i for i in range(x,y+1)]
a.pop(1)
a.pop(-2)
print(a)

