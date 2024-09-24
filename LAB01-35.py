# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:21:12 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 0
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range(1, n + 1):
    S += i
print(f"Tổng S từ 1 đến {n} là: {S}")
