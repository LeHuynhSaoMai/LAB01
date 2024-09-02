# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:15:16 2024

@author: User
"""


a = float(input("Nhập a ="))
b = float(input("Nhập b ="))
if a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Ngiệm của phương trình là x =", (-b/a))