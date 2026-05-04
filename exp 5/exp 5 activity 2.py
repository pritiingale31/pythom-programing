# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:47:33 2026

@author: priti ingle
"""
# Roll numbers present in Class A and Class B
class_a = {101, 102, 105, 108, 110}
class_b = {102, 103, 105, 107, 110}

# Find students present in both (Intersection)
both_present = class_a.intersection(class_b)

print(f"Students present in both classes: {both_present}")

