# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:23:57 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương chẵn n: "))
s = 0
while n <= 0 and n % 2 != 0:
    n = int(input("n phải là số nguyên dương chẵn. Nhập lại n: "))
for i in range (2, n + 1, 2):
   s += i
print(f"Tổng s từ 2 đến {n} là: {s}")
