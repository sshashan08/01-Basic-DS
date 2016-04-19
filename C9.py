# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:50:49 2016

@author: shashank
"""

import math

X=[1,2,3,4,5]
Y=[10,20,30,40,50]

XY = 0
Xi = 0
Yi = 0
Xi2 = 0
Yi2 = 0


for i in range(0,5,1):
    XY += X[i]*Y[i]
    Xi += X[i]
    Yi += Y[i]
    Xi2 += X[i]**2
    Yi2 += Y[i]**2

R = (XY - (Xi*Yi)/5) / (math.pow((Xi2 - ((Xi)**2)/5),0.5)*math.pow((Yi2 - ((Yi)**2)/5),0.5))

print(R)

#Try using Zip

