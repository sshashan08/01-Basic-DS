# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:41:23 2016

@author: shashank
"""

#UserXRatingsD = {'A':1, 'B':2, 'D':4, 'E':5}
#UserYRatingsD = {'A':10, 'B':20, 'C':30, 'D':40, 'E':50}

#X = set(sorted(UserXRatingsD.keys()))
#Y = set(sorted(UserYRatingsD.keys()))
#
#intersection = X & Y
#
#
#for i in sorted(intersection):
#    print(i," ", UserXRatingsD[i], " " , UserYRatingsD[i])
#    

import C15DictImp

UserRatingsND = {'X':{'A':1, 'B':2, 'D':4, 'E':5}, 'Y': {'A':10, 'B':20, 'C':30, 'D':40, 'E':50} }

print(UserRatingsND['X'])

K = UserRatingsND.keys()

for i in enumerate(sorted(K)):
    if i == 0:
        UserXRatingsD = UserRatingsND[i]
    if i == 1:
        UserYRatingsD = UserRatingsND[i]


sim = C15DictImp.measure(UserXRatingsD,UserYRatingsD)

md = sim.minkowiski(1)
print("Manhattan Distance: ", round(md,2))

md = sim.minkowiski(2)
print("Manhattan Distance: ", round(md,2))

md = sim.minkowiski(3)
print("Manhattan Distance: ", round(md,2))

corr =sim.pearson()
print("Correlation: ", round(corr,2))
