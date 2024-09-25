# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:57:24 2024

@author: Admin
"""

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = 0
mau_so = 0
for i in range(1, n+1):
  mau_so += i
  S += x**i / mau_so
print("Tổng S(n) =", S)
