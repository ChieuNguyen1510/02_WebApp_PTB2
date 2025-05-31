import streamlit as st
import math

st.title("Giải Phương Trình Bậc 2")

# Nhập hệ số
a = st.number_input("Nhập a", value=1.0)
b = st.number_input("Nhập b", value=0.0)
c = st.number_input("Nhập c", value=0.0)

if st.button("Giải"):
    if a == 0:
        if b == 0:
            st.write("Không phải phương trình.")
        else:
            x = -c / b
            st.write(f"Phương trình bậc nhất. Nghiệm x = {x:.2f}")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            st.write("Phương trình vô nghiệm.")
        elif delta == 0:
            x = -b / (2*a)
            st.write(f"Phương trình có nghiệm kép x = {x:.2f}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            st.write(f"Nghiệm x1 = {x1:.2f}, x2 = {x2:.2f}")
