# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:53:15 2026

@author: prit
import streamlit as st

st.title("🛒 Simple Grocery Bill Calculator")

# Input for items
item_name = st.text_input("Item Name", "Milk")
price = st.number_input("Price per Unit", min_value=0.0, value=1.0, step=0.1)
quantity = st.number_input("Quantity", min_value=1, value=1)
tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, value=5.0)

# Calculate total
if st.button("Add to Bill"):
    total = price * quantity
    tax_amount = total * (tax_rate / 100)
    final_total = total + tax_amount
    
    st.success(f"{item_name} (x{quantity}): ${final_total:.2f}")
    st.write(f"Breakdown: ${total:.2f} + ${tax_amount:.2f} tax")
