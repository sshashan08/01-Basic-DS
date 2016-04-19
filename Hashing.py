# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:01:36 2016

@author: shashank

Hash Table Implementations
"""

class HashTables:
    
    def __init__(self, Size):
        self.size = Size
        self.map = [None]*self.size
        
    def get_hash(self, Key):
        hash_value = 0
        for i in Key:
            hash_value += ord(i)
        return hash_value %self.size
        
    
    def adding(self, Key, Val):
        hash_value = self.get_hash(Key)
        keyVal = [Key, Val]
        
        if self.map[hash_value] is None:
            self.map[hash_value] = list([keyVal])
        else:
            for pairs in self.map:
                if pairs[0] == Key:
                    pairs[1] = Val
                    return True
            self.map.append([keyVal])
            
    def search(self, Key):
        hash_value = self.get_hash(Key)
        
        if self.map[hash_value] is None:
            return None
        else:
            for pairs in self.map[hash_value]:
                if pairs[0] ==Key:
                    return pairs[1]
            return None
            
    def delete(self, Key):
        hash_value = self.get_hash(Key)
        if self.map[hash_value][0] is None:
            return None
        else:
            for i in range(0, len(self.map[hash_value])):
                if self.map[hash_value][i][0] == Key:
                    return self.map[hash_value].pop(i)
            return None
    
    


h = HashTables(Size = 3)

h.adding("Shashank", 646)
h.adding("Chida", 234)
h.adding("Sai", 865)
h.adding("Ankita", 867)
            
            