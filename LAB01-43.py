# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:56:26 2024

@author: Admin
"""

n = int(input("Nhập n: "))
S = 0
for i in range(1, n+1):
    S += i / (i+1)
print("Tổng S(n) =", S)
