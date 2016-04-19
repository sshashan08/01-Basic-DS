# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:19:34 2016

@author: shashank
"""


import math

class measure:
    
    def __init__(self, Ratings1, Ratings2):
        self.r1 = Ratings1
        self.r2 = Ratings2
    
    def minkowiski(self, r):
        dist = 0
                
        X = set(sorted(self.r1.keys()))
        Y = set(sorted(self.r2.keys()))  
        intersection = X & Y
        
        for x in sorted(intersection):
            dist += pow(abs(self.r1[x]-self.r2[x]),r)

        return pow(dist,1/r)
    
    def pearson(self):
        XY = 0
        Xi = 0
        Yi = 0  
        Xi2 = 0
        Yi2 = 0

        X = set(sorted(self.r1.keys()))
        Y = set(sorted(self.r2.keys()))  
        intersection = X & Y
        
        for i in intersection:
            XY += self.r1[i]*self.r2[i]
            Xi += self.r1[i]
            Yi += self.r2[i]
            Xi2 += self.r1[i]**2
            Yi2 += self.r2[i]**2

        R = (XY - (Xi*Yi)/5) / (math.pow((Xi2 - ((Xi)**2)/5),0.5)*math.pow((Yi2 - ((Yi)**2)/5),0.5))

        return (R)
    