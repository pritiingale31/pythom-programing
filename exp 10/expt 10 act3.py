# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:58:18 2026

@author: priti ingale
"""

import streamlit as st

st.title("📊 Student Result Calculator")

# Subjects
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = {}

st.write("Enter marks out of 100:")
for subject in subjects:
    marks[subject] = st.number_input(f"{subject} Marks", min_value=0.0, max_value=100.0, value=0.0)

if st.button("Calculate Result"):
    total_marks = sum(marks.values())
    percentage = (total_marks / (len(subjects) * 100)) * 100
    
    st.subheader(f"Total Marks: {total_marks} / {len(subjects) * 100}")
    st.subheader(f"Percentage: {percentage:.2f}%")
    
    # Simple Grading
    if percentage >= 90:
        st.success("Grade: A+")
    elif percentage >= 75:
        st.success("Grade: A")
    elif percentage >= 50:
        st.warning("Grade: B")
    else:
        st.error("Grade: F (Fail)")
