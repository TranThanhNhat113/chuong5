# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:58:45 2024

@author: PC
"""

N = int(input("Nhập vào một số nguyên dương N: "))
tong = sum(int(i) for i in str(N))
print("Tổng các chữ số là:", tong)
