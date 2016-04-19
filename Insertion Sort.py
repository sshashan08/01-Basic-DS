# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:07:42 2016

@author: shashank

Purpose: Insertion Sort
"""

def InsertionSort(Ar):
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
    
    j = 0
    for i in range(0,l-1,1):
        
        if (Ar[i+1] < Ar[i]):
            j = i
            temp = Ar[j+1]
            Ar[j+1] = Ar[j]
            Ar[j] = temp
            
            while (j >= 1 and Ar[j-1] > Ar[j]):
                temp = Ar[j-1]
                Ar[j-1] = Ar[j]
                Ar[j] = temp
                j -= 1

    return Ar
    
Ar = [23, 17, 32, 21, 1, 19, 5, 12, 9, 11]

InsertionSort(Ar)