# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:58 2026

@author: priti ingale
"""

def register_user(age):
    try:
        age = int(age) # Ensure age is a number
        if age < 0 or age > 120:
            return "Invalid Age: Age must be between 0 and 120."
        else:
            return f"Registration Successful! Age: {age}"
    except ValueError:
        return "Invalid Input: Please enter a numeric age."

# Example Usage
print(register_user("twenty")) # ValueError
print(register_user(150))      # Invalid age
print(register_user(25))       # Valid
