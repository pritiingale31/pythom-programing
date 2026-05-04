# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:23:40 2026

@author:  priti ingale
"""
def split_bill(total, people):
    try:
        share = total / people
        return f"Each person pays: ${share:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide bill among zero people."

# Example Usage
print(split_bill(100, 4)) # Success
print(split_bill(100, 0)) # Prevents Crash

