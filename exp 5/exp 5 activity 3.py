# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:48:07 2026

@author: priti ingale
"""
inventory = {"Notebooks": 50, "Pens": 100}

def add_stock(item, quantity):
    if item in inventory:
        inventory[item] += quantity  # Increase existing quantity
    else:
        inventory[item] = quantity   # Add new item to inventory

# Adding stock
add_stock("Pens", 20)      # Updates Pens to 120
add_stock("Erasers", 30)   # Adds new entry for Erasers

print(f"Current Inventory: {inventory}")

