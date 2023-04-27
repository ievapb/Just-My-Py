# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:30:55 2020

@author: ieva
"""


s = input ()
order = 'abcdefghijklmnopqrstuvwxyz'
substring = ' '
sub = ' '
for i in range(len(s)):
    if s[i:i+2] == order[i:i+2]:
        sub += s[i: i+2]
        i += 1
    if len(substring) < len(sub):
        substring = sub
        sub = ' '
print ('Longest substring in alphabetical order is:', substring)