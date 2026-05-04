# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:56:39 2026

@author: priti sunil ingale
"""

import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
st.title("⚖️ BMI Health Checker")

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=30.0, step=0.1)

# Calculation
if st.button("Calculate BMI"):
    if weight and height:
        height_m = height / 100  # convert cm to meters
        bmi = weight / (height_m ** 2)
        
        st.subheader(f"Your BMI is: {bmi:.2f}")
        
        # Categorization
        if bmi < 18.5:
            st.warning("You are underweight 🥦")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight ✅")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight ⚠️")
        else:
            st.error("You are obese 🚨")
