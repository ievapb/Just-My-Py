# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 01:34:06 2020

@author: ieva
"""


"""
Write a function called longestRun, which takes as a parameter 
a list of integers named L (assume L is not empty). This function 
returns the length of the longest run of monotonically 
increasing numbers occurring in L. A run of monotonically 
increasing numbers means that a number at position k+1 in 
the sequence is either greater than or equal to the number 
at position k in the sequence.

For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your 
function should return the value 5 because the longest run of 
monotonically increasing integers in L is [3, 4, 5, 7, 7].

"""

def longestRun(L):
    subs={}
    subl = []
    if len(L) == 1:
        return 1
    else:
        for e in L:
            i = L.index(e)
            if i == (len(L)-1):
                subs[len(subl)] = subl
                break
            subl.append(e)
            if e == L[i+1] or e < L[i+1]:
                pass
            else:
                subs[len(subl)] = subl
                subl.clear()
        keys = subs.keys()      
        return max(keys)
    
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 8, 2] 
print(longestRun(L))
L = [1, 1, 1, 1]
print(longestRun(L))
