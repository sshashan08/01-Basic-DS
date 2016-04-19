# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:43:34 2016

@author: shashank

Purpose: Merge Sort

"""


def MergeSort(Ar):
    l = len(Ar)
    
    if l < 2:
        return Ar
    
    Ar1 = MergeSort(Ar[0:(l//2)])
    Ar2 = MergeSort(Ar[(l//2):l])
    
    return Merging(Ar1, Ar2)


def Merging(Ar1, Ar2):

    A = []
    while(len(Ar1)>0 and len(Ar2)>0):
        if(Ar1[0] < Ar2[0]):
            A.append(Ar1.pop(0))
        else:
            A.append(Ar2.pop(0))
    
    while(len(Ar1) > 0):
        A.append(Ar1.pop(0))
        
    while(len(Ar2) > 0):
        A.append(Ar2.pop(0))
    
    return A


Ar = [23, 17, 32, 21, 1, 19, 5, 12, 9, 11]

print(MergeSort(Ar))