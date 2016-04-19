# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 09:33:49 2016

@author: shashank
"""

import C12

UX = [1,2,3,4,5]
UY = [10,20,30,40,50]

sim = C12.measure(UX,UY)

md = sim.minkowiski(1)
print("Manhattan Distance: ", round(md,2))

md = sim.minkowiski(2)
print("Manhattan Distance: ", round(md,2))

md = sim.minkowiski(3)
print("Manhattan Distance: ", round(md,2))

corr = sim.pearson()
print("Correlation: ", corr)