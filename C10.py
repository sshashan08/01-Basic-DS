# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:10:55 2016

@author: shashank
"""

UserXRatings = [1,2,3,4,5]
UserYRatings = [10,20,30,40,50]


def minkowiskil(ratings1, ratings2,r):
    MinkowiskiDist = 0

    for i in range(len(ratings2)):
        MinkowiskiDist += math.pow(abs(ratings1[i] - ratings2[i]),r)

    MinkowiskiDist = MinkowiskiDist**(1/r)

    print("Minkowiski Distance: ",MinkowiskiDist)

minkowiskil(UserXRatings,UserYRatings,1)
minkowiskil(UserXRatings,UserYRatings,2)
minkowiskil(UserXRatings,UserYRatings,3)
