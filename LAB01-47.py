# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:58 2024

@author: Admin
"""

danhsach = []
max_sum = 0
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                current_sum= x+y+z
                if current_sum > max_sum:
                    max_sum = current_sum
                    danhsach = [(x,y,z)]
if danhsach:
    x, y, z = danhsach[0]
    print(f"Nghiệm: x = {x}, y = {y}, z = {z} với tổng x + y + z = {max_sum}")
else:
    print("Không tìm thấy nghiệm nào.")
