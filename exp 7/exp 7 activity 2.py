# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:54:01 2026

@author: priti ingale
"""
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_total_salary(self, bonus_percentage):
        bonus = (bonus_percentage / 100) * self.base_salary
        return self.base_salary + bonus

# Usage
emp = Employee("Rahul", 50000)
total = emp.calculate_total_salary(10) # 10% bonus
print(f"Total Salary for {emp.name}: ₹{total}")

