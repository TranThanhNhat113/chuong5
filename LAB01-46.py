# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:19 2024

@author: Admin
"""

for x in range(1, 490):
    for y in range(1, (979 - 2 * x) // 7 + 1):
        z = (979 - 2 * x - 7 * y) / 9
        if z > 0 and z.is_integer():
            print(f"x = {x}, y = {y}, z = {int(z)}")
