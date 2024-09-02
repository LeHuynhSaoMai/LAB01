# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:05:54 2024

@author: Smai
"""

a=int(input("Số nguyên a: "))
b=int(input("Số nguyên b: "))
c=int(input("Số nguyên c: "))
if a>c and a>b:
    print("Số có giá trị lớn nhất là:",a)
elif b>a and b>c:
    print("Số có giá trị lớn nhất là:",b)        
else:
    print("Số có giá trị lớn nhất là:",c)