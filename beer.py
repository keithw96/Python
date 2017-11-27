# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:57:53 2017

@author: gameuser
"""

for i in range(99,0,-1):
    if i is not 1:
        print(i, "bottles of beer on the wall")
        print(i, "bottles of beer")
    elif i is 1 :
        print(i, "bottle of beer on the wall")
        print(i, "bottle of beer")
    print("take one down")
    print("pass it around")
    if i is not 1:
        print(i - 1, "bottles of beer on the wall \n")
    else:
        print("no more bottles of beer on the wall")
