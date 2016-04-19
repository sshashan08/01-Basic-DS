# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:39:01 2016

@author: shashank

Purpose: Bubble Sort
"""

def BubbleSort(Ar):
    l = len(Ar)
    
    if (l==0):
        raise ValueError("Empty Array !!")
        return None
    
    elif (l==1):
        print("Array already sorted!!")
        return Ar
    
    flag = 0
    
    for i in range(0,l-1):
        if (Ar[i+1] < Ar[i]):
            flag = 1
    
    if (flag == 0):
        print("array already sorted !!")
        return Ar
    
    
    for i in range(0,l-1,1):
        for j in range(0,l-i-1,1):
            if(Ar[j+1] < Ar[j]):
                temp = Ar[j]
                Ar[j] = Ar[j+1]
                Ar[j+1] = temp
    
    return Ar



Ar = [23, 17, 32, 21, 1, 19, 5, 12, 9, 11]

BubbleSort(Ar)


    
    