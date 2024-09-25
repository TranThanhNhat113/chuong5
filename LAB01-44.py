# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:57:09 2024

@author: Admin
"""

n = int(input("Nhập n: "))
tong = 0
for i in range(n+1):
    tong += (2*i + 1) / (2*i + 2)
print("Tổng S(n) =", tong)
