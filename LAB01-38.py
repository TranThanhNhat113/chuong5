# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:25:10 2024

@author: PC
"""

n = int(input("Nhập vào số nguyên dương lẻ n để tính(1 * 2 * 3 * ... * n) : "))
s = 1
while n <= 0 or n % 2 ==0 :
    n = int(input("n phải là số nguyên dương lẻ. Nhập lại N: "))
for i in range (1, n + 1):
   s = s * i
print("Kết quả là: ",s)
