# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:22:36 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương n: "))
s = 0
while n <= 0:
    n = int(input("n phải là số nguyên dương. Nhập lại n: "))
for i in range (1, n + 1):
   s += i ** 2
print(f"Tổng S từ 1^2 đến {n}^2 là: {S}")
    
