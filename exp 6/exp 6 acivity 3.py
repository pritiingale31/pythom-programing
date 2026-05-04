# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:51:30 2026

@author: priti inagle
"""
# Creating a dummy complaint file first
with open("complaints.txt", "w") as file:
    file.write("1. Water leakage in Lab 2\n2. AC not working in Hall A")

# Reading and displaying complaints
print("--- Registered Complaints ---")
try:
    with open("complaints.txt", "r") as file:
        content = file.read()
        print(content if content else "No complaints found.")
except FileNotFoundError:
    print("Complaint file does not exist yet.")

