# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:19:16 2016

@author: shashank
"""

import math

UserXRatings=[1,2,3,4,5]
UserYRatings=[10,20,30,40,50]

def pearsonl(X,Y):
    
    if (len(X) != len(Y)):
        print("Error: Ranges are not of same length!")
        goto last;
    if len(X)==0 or len(Y)==0 :
        print("Error: Ranges are empty!")
        goto last;
        
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

    R = (XY - (Xi*Yi)/len(X)) / (math.pow((Xi2 - ((Xi)**2)/len(X)),0.5)*math.pow((Yi2 - ((Yi)**2)/len(X)),0.5))

    return R
    label: last

print(pearsonl(UserXRatings, UserYRatings))
rx = []
ry = []
print(pearsonl(rx,ry))

