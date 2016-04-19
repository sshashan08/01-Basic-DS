# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 01:01:27 2016

@author: shashank

Binary Search
"""

class BinarySearch:
    
    def __init__(self, Arr):
        self.Array = Arr
        self.length = len(self.Array)
        
    def validation(self):
        if type(self.Array) != type([]):
            raise ValueError("Not a list!")
            return None

        mid = self.length//2
        
        if not (((self.Array[0] < self.Array[mid]) and (self.Array[mid] < self.Array[self.length-1])) or ((self.Array[0] > self.Array[mid]) and (self.Array[mid] > self.Array[self.length-1]))):
            raise ValueError ("Array not Sorted!")
            return None
    
    def SearchB(self, x):
        upper = self.length -1
        lower = 0
        mid = lower + (upper - lower)//2
        
        Found = False
        
        while Found == False and upper > lower:
            
            if upper < lower:
                print("Value Not Found!")
                return None
            
            if x < self.Array[mid]:
                upper = mid -1
                mid = lower + (upper - lower)//2
                
            if x > self.Array[mid]:
                lower = mid +1
                mid = lower + (upper - lower)//2
            
            if x == self.Array[mid]:
                Found = True
                return mid
    

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

Bin = BinarySearch(A)

Bin.validation()
Bin.SearchB(32)


A1 = list(range(2,40,2))

B2 = BinarySearch(A1)
B2.validation()

B2.SearchB(30)

