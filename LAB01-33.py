# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:15:15 2024

@author: PC
"""

import math
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải là số nguyên dương. Nhập lại n: "))
if int(math.sqrt(n)) ** 2 == n:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải là số chính phương")
