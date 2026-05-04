# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:59:43 2026

@author: shruti jadhav
"""
# Traffic Police System
speed = float(input("Enter driver speed (km/h): "))

if speed > 60:
    print("Fine Message: Overspeeding detected! Speed limit exceeded.")
else:
    print("Speed is within limits. Safe driving.")

