# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:01:22 2016

@author: shashank
"""

for i in range(1,6,1):
    print(" "*(7-i), end = "")    
    for j in range(1,i+1,1):
        print(j, end="")
    for j in range(i,1,-1):
        print(j-1, end="")
    print("\n")

for i in range(6,0,-1):
    print(" "*(7-i), end = "")    
    for j in range(1,i+1,1):
        print(j, end="")
    for j in range(i,1,-1):
        print(j-1, end="")
    print("\n")