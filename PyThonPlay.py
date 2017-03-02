# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import this # The Zen of Python
import random
import math
import pandas
import matplotlib as graph
import sys, os
# sys.exit() terminates a program or script

#from random import * 
"""
    With this form of import statement,
    calls to functions in random will not
    need the random. prefix
"""

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

print(days[1][:3])

x , w = 1, 2


#For mday in range(days)

print("a" * w**w**w)


#print(type(input("Please type your name: ")))

print(random.random()**w/x)

print(int(math.pi))

print(int(3.500000000001*10)/10)

w = w * random.random()

if w > 1.5:
    print("Mate, it's cooked: " + str(w) +"!")
elif w<=1 and w>0.5:
    print("What's the drill now?")
else:
    print("Clucking bells!")

n = 0    
while w > (2*x) * random.random():
    if n >= 10:
        break
    elif int((10*random.random()))%2 !=0:
        print("Even number found!")
        continue
    print("It's cooking mate:", w)
    w = w * random.random()
    n = n +1

m=517
h, t = 0.0, 0.0

for n in range(1, m+1):
    if random.random() < 0.5:
        h=h+1
    else:
        t=t+1
        
for n in range(0,10,1):
    print(n)

print(round(100*h/m,0), round(100*t/m,0))

print(not(bool(0.0!=0)))

for n in range(10,0,-2):
    print(n, random.randint(1,10))


