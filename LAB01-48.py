# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:01:56 2024

@author: Admin
"""

min_sum = float('inf') 
solutions = []  
for x in range(1, 490):
    for y in range(1, (979 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z > 0 and z.is_integer():
            z = int(z)
            current_sum = x + y + z
            if current_sum < min_sum:
                min_sum, solutions = current_sum, [(x, y, z)]
            elif current_sum == min_sum:
                solutions += [(x, y, z)]
if solutions:
    print(f"Tổng nhỏ nhất x + y + z là: {min_sum}")
    for sol in solutions:
        print(f"x = {sol[0]}, y = {sol[1]}, z = {sol[2]}")
