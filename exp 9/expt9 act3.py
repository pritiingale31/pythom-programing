# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:16:03 2026

@author: priti ingale
"""

import math

def euclidean_distance(p1, p2):
    # p1 and p2 are tuples like (x, y)
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Alternative using built-in math.dist (Python 3.8+)
point_a = (3, 4)
point_b = (7, 1)
distance = math.dist(point_a, point_b)

print(f"Euclidean Distance: {distance}")
