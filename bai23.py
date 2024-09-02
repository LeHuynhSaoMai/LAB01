# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:13:23 2024

@author: User
"""

# Nhập các hệ số 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = 0
delta = b**2 - 4*a*c
print ("Giải phương trình bậc 2: ax^2 + bx + c = 0")
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x =", -b/(2*a))
else:
    print("Phương trình có hai nghiệm phân biệt", (-b + delta**0.5)/(2*a), "và", (-b + delta**0.5)/(2*a))