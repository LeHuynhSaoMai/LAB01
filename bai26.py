# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:56:44 2024

@author: 
"""
#a
print ("a.")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần: ", a, b, c)
#b
print("b.")
N = input("Nhập số nguyên: ")
dayso = "".join(sorted(N))
print("Dãy số theo thứ tự tăng dần: ", dayso)