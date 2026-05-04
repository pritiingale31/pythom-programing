# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:22:08 2026

@author: priti ingale
"""

def withdraw_cash(balance, amount):
    if amount > balance:
        return f"Transaction Failed: Insufficient funds. Balance: ${balance}"
    else:
        balance -= amount
        return f"Withdrawal Successful! Remaining Balance: ${balance}"

# Example Usage
print(withdraw_cash(500, 200)) # Success
print(withdraw_cash(500, 600)) # Insufficient
