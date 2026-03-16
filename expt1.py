# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:58:48 2026

@author: priti
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()"""
num1=int(input("Enter Number1:"))
num2=int(input("Enter Number2:"))

sum=num1+num2
print("Addition=",sum)

sub=num1-num2
print("Substraction=",sub)

mul=num1*num2
print("Multiplication=",mul)

div=num1/num2
print("Division=",div)

mod=num1%num2
print("Modulus=",mod)