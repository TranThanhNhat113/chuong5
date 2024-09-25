# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:48:50 2024

@author: Admin
"""
n = int(input("Nhập giá trị n: "))
s = 0
for i in range(1, n+1):
  s += 1/i
print("Tổng S(n) =", s)


