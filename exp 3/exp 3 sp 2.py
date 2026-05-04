# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:28:43 2026

@author: priti ingale
"""

def simple_interest(principal, rate, time):
si = (principal * rate * time) / 100
return si
# Taking input from the user
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
# Function call
interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)