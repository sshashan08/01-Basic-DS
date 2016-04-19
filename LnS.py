# -*- coding: utf-8 -*-
"""
Created: Tue Feb 16 23:55:13 2016
@author: shashank
Problem: "Look and Say" Sequence
Version: 1.0
"""


#defining the function to print this sequence for a selected number of rows
def LnS(n):
    # Variable to hold the sequence to be printed    
    SequenceLnS = 1*[None]
    
    i=0
    while i<=n:
        # Variable for holding the number and its count
        val = 1*[None]
        cnt = 1*[None]

        # Counter to trace the previous row sequence
        j=0
        
        # Handling first row
        if i==0:
            SequenceLnS[0]=1
            print(SequenceLnS)
        
        # handling remaining rows
        else:
            val[0] = SequenceLnS[j]
            cnt[0] = 1
            
            # Seperating numbers and their counts
            for k in range(1,len(SequenceLnS),1):
                if SequenceLnS[k]==None or SequenceLnS[k]==0:
                    pass                   
                elif val[j]==SequenceLnS[k]:
                    cnt[j] += 1
                elif val[j]!=SequenceLnS[k]:
                    j += 1
                    val.append(SequenceLnS[k])
                    cnt.append(1)
        l = 2*len(cnt)
        SequenceLnS = l*[None]
        SequenceLnS[0:l-1:2] = cnt
        SequenceLnS[1:l:2] = val
        
        # Printing the sequence
        for m in SequenceLnS:
            if m != None:            
                print(m, end=" ")
        i += 1
        print()


n = int(input("Enter the number of rows to be printed: "))
LnS(n)

    