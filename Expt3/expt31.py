# program to print the pattern
"""
Created on Mon Feb 16 04:38:29 2026

@author: priti
"""
n=int (input  ( "enter number of rows  :"))
for i in range  (1,n+1) :
    for j in range  (1,i+1) :
        print (j,end= " ")
    print ()
