# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:01:56 2024

@author: Admin
"""

danhsach = []
min_sum = float('inf')
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2 * x + 7 * y + 9 * z == 979:
                current_sum = x + y + z
                if current_sum < min_sum:  # Kiểm tra tổng nhỏ nhất
                    min_sum = current_sum
                    danhsach = [(x, y, z)]  # Cập nhật danh sách
if danhsach:
    x, y, z = danhsach[0]
    print(f"Nghiệm: x = {x}, y = {y}, z = {z} với tổng x + y + z = {min_sum} nhỏ nhất")
else:
    print("Không tìm thấy nghiệm nào.")
