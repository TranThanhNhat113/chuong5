# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:59:19 2024

@author: Admin
"""

danhsach = []
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x + 7*y + 9*z == 979:
                danhsach += [(x,y,z)] 
if danhsach:
    for i in danhsach:
        print("Bộ nghiệm: ", i)
else:
    print("Không tìm thấy bộ nghiệm nào.")
