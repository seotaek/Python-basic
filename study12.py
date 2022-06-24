# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:40:35 2022

@author: gprua
"""

#12딕셔너리 사용하기
lux={'health':490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72}
print(lux['health'])#중복된 키의 정보는 맨뒤의 값만 사용

x={100: 'hundred', False: 0, 3.5:[3.5,3.5]}
#키에는 리스트와 딕셔너리를 사용할 수 없다

#딕셔너리 생성방법
lux=dict(heath=490,mana=334,melee=550,armor=18.72)
lux=dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
lux=dict([('health',490),('mana',334),('melee',550),('armor',18.72)])

#키에 값을 할당하기
lux['mana_regen']=3.28
print(lux)
print(lux['mana_regen'])
print('health' in lux)

#12.4
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
 
print(camille['health'])
print(camille['movement_speed'])

#12.5
x=map(float,input().split())
y=input().split()
z=dict(zip(y,x))
print(z)