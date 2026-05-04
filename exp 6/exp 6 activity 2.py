# -*- coding: utf-8 -*-
"""
Created on Mon May  4 09:51:00 2026

@author: priti ingale
"""
def mark_attendance(roll_no, status):
    with open("attendance.txt", "a") as file:
        file.write(f"Roll No: {roll_no}, Status: {status}\n")
    print("Record added successfully.")

# Adding new records
mark_attendance("101", "Present")
mark_attendance("102", "Absent")

