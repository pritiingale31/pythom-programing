# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:03:35 2026

@author: priti ingale
"""

import math
from datetime import date

# 1. Calculate EMI Interest
# Formula for EMI: [P x R x (1+R)^N]/[(1+R)^N-1]
def calculate_emi(p, annual_rate, n):
    r = annual_rate / (12 * 100)  # Monthly interest rate
    emi = (p * r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)
    
    # Interest for the first month = Principal * monthly rate
    interest_first_month = p * r
    return emi, interest_first_month

# 2. Display Today's Date (Hospital Appointment System)
today = date.today().strftime("%B %d, %Y")

# 3. Calculate Distance using the Distance Formula
# Distance = sqrt((x2-x1)^2 + (y2-y1)^2)
def get_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# --- Examples ---
# EMI Example: Principal 500,000, 8.5% annual rate, 24 months
emi_val, interest = calculate_emi(500000, 8.5, 24)

# Distance Example: Distance between (0,0) and (3,4)
dist = get_distance(0, 0, 3, 4)

print(f"1. EMI: {emi_val:.2f} | Interest portion of first payment: {interest:.2f}")
print(f"2. Appointment Date: {today}")
print(f"3. Euclidean Distance: {dist}")
