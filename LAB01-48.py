# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:01:56 2024

@author: Admin
"""

min_sum = float('inf') 
ds = []  
for x in range(1, 490):
    for y in range(1, (979 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z > 0 and z.is_integer():
            z = int(z)
            tong = x + y + z
            if tong < min_sum:
                min_sum, ds = tong, [(x, y, z)]
            elif tong == min_sum:
                ds += [(x, y, z)]
if ds:
    print(f"Tổng nhỏ nhất x + y + z là: {min_sum}")
    for x, y, z in ds:
        print(f"x = {x}, y = {y}, z = {z}")
