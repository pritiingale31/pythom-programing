# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:15:04 2026

@author: priti ingale
"""

import math
from datetime import date

# 1. EMI Calculation (Interest part of the first payment)
# Formula: EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / (math.pow(1 + monthly_rate, tenure_months) - 1)
    # Interest for the first month
    interest_paid = principal * monthly_rate
    return emi, interest_paid

# 2. Today's Date for Hospital Appointment
today = date.today().strftime("%B %d, %Y")

# 3. Distance Formula (Euclidean distance between two points)
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Examples
p, r, n = 500000, 8.5, 24
emi, int_val = calculate_emi(p, r, n)
dist = calculate_distance(0, 0, 3, 4)

print(f"EMI: {emi:.2f}, First Month Interest: {int_val:.2f}")
print(f"Hospital Appointment Date: {today}")
print(f"Distance between (0,0) and (3,4): {dist}")