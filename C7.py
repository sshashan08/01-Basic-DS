# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:53:16 2016

@author: shashank
"""

import math

BilledAmt = 1000
TipPercent = 10

TotalDue = ((100+TipPercent)/100)*BilledAmt

print("Billed Amount: ", BilledAmt, "\t Tip %: ", TipPercent, "%", "Total Amount: ",TotalDue)


mySchool = "I Study at ASU"

print(mySchool)

for i in range(0,math.floor(len(mySchool)/2),1):
    print(mySchool[i], end="")

print("\n")

for i in range(math.floor(len(mySchool)/2)+1,len(mySchool),1):
    print(mySchool[i], end="")
print("\n")

print(mySchool[::-1])

print("".join(reversed(mySchool)))



print("\n")
print(mySchool[::1])

print(mySchool.find("ASU"))

x1 = 1
y1 = 2

x2 = 10
y2 = 20

DistanceMhtn = abs(x1 - x2) + abs(y1 - y2)

DistanceEuc = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

DistanceMink = math.pow((abs((x1 - x2)**3) + abs((y1 - y2)**3)),(1/3))

print("Manhattan Distance: ", DistanceMhtn)
print("Manhattan Distance: ", DistanceEuc)
print("Manhattan Distance: ", DistanceMink)