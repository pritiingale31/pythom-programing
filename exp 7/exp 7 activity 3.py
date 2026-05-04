# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:54:40 2026

@author: priti inagle
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90: return "A+"
        elif self.marks >= 75: return "A"
        elif self.marks >= 60: return "B"
        elif self.marks >= 35: return "C"
        else: return "Fail"

# Usage
s1 = Student("Ananya", 82)
print(f"Student: {s1.name}, Grade: {s1.get_grade()}")

