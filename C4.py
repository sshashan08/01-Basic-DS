# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:52:53 2016

@author: shashank
"""

tup = (1,2,3,4,5)

print("#", tup, len(tup), tup[2:4])

matr = ((1,2,3),(4,5,6),(7,8,9))

print("##", matr[2][0])

M1,M2,M3 = matr

print("###", M1, "\t", M2, "\t", M3)
print("####", M1[1], "\t", M2[0], "\t", M3[2])

lst = list(M1)

lst[1]=10000

M1 = tuple(lst)

print("######", M1)