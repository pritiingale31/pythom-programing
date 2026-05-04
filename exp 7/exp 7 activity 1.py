# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:53:13 2026

@author: priti ingale
"""
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")

# Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

