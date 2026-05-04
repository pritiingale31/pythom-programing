# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:07:23 2026

@author: priti ingle
"""
# Program to check movie entry eligibility
try:
    # Take user input for age and convert to integer
    age = int(input("Enter your age: "))

    # Check eligibility condition (age >= 18)
    if age >= 18:
        print("Entry Allowed: You are eligible to watch the movie.")
    else:
        print("Entry Denied: You must be at least 18 years old.")
except ValueError:
    print("Invalid input. Please enter a valid numerical age.")

