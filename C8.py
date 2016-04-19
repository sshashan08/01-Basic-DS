# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:20:32 2016

@author: shashank
"""

UserXRatings = [1,2,3,4,5]
UserYRatings = [10,20,30,40,50]

ManhattanDist = 0

for i in range(5):
    ManhattanDist += abs(UserXRatings[i] - UserYRatings[i])

print("Manhattan Distance: ",ManhattanDist)


EuclideanDist = 0

for i in range(5):
    EuclideanDist += math.pow(abs(UserXRatings[i] - UserYRatings[i]),2)

print("Euclidean Distance: ",EuclideanDist**(1/2))


MinkowiskiDist = 0

for i in range(5):
    MinkowiskiDist += math.pow(abs(UserXRatings[i] - UserYRatings[i]),3)

print("Minkowiski Distance: ",MinkowiskiDist**(1/3))