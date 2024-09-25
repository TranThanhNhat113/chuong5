# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:58 2024

@author: Admin
"""

solutions = []

for x in range(1, 490):
    for y in range(1, (979 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z > 0 and z.is_integer():
            z = int(z)
            solutions += [(x, y, z)]  # Thay thế append bằng toán tử cộng

# Tìm tổng lớn nhất và in ra kết quả
if solutions:
    max_sum = max(sum(solution) for solution in solutions)
    print(f"Tổng lớn nhất x + y + z là: {max_sum}")
    for x, y, z in solutions:
        if x + y + z == max_sum:
            print(f"x = {x}, y = {y}, z = {z}")
