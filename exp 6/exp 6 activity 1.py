# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:49:46 2026

@author: priti ingale
"""
# Writing expenses to the file
with open("expenses.txt", "w") as file:
    file.write("500\n200\n1250\n450")

# Calculating the total
total_expense = 0
with open("expenses.txt", "r") as file:
    for line in file:
        total_expense += float(line.strip())

print(f"Total Monthly Expense: ₹{total_expense}")

