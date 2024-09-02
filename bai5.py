# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:49:42 2024

@author: Smai
"""

h=int(input("Nhập giờ: "))
m=int(input("Nhập phút: "))
s=int(input("Nhập giây: "))
print("Thời gian đã nhập: ",f"{h}:{m}:{s}")
print("Thời gian theo giây: ", h*3600+m*60+s,"(s)")