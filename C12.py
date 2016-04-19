# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:22:26 2016

@author: shashank
"""

import math

class measure:
    
    def __init__(self, Ratings1, Ratings2):
        self.r1 = Ratings1
        self.r2 = Ratings2
    
    def minkowiski(self, r):
        dist = 0
    
        for x,y in zip(self.r1, self.r2):
            dist += pow(abs(x-y),r)

        return pow(dist,1/r)
    
    def pearson(self):
        XY = 0
        Xi = 0
        Yi = 0  
        Xi2 = 0
        Yi2 = 0


        for i in range(0,len(self.r1),1):
            XY += self.r1[i]*self.r2[i]
            Xi += self.r1[i]
            Yi += self.r2[i]
            Xi2 += self.r1[i]**2
            Yi2 += self.r2[i]**2

        R = (XY - (Xi*Yi)/5) / (math.pow((Xi2 - ((Xi)**2)/5),0.5)*math.pow((Yi2 - ((Yi)**2)/5),0.5))

        return (R)
    