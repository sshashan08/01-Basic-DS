# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:28:09 2016

@author: shashank
"""

ListPeople = ["Tom","Dick","Harry"]
ListNum = [1,2,3,4,4,4,4,4,4]

Absurd = [1,"As", "T", 0x32]

print(ListPeople)
print(ListNum)
print(Absurd)

print("###", ListPeople)

ListPeople.append("Shashank")

print("####", ListPeople)

ListPeople.extend(Absurd)

ListPeople.extend(ListNum)

print("#####", ListPeople)

ListPeople.remove("As")
del ListPeople[3]
ListPeople.pop()



print("######", ListPeople, ListPeople.count("Tommy"))

