import streamlit as st
import math

def run():
    st.header("📐 Giải Phương Trình Bậc 2")
    a = st.number_input("Nhập a", value=1.0)
    b = st.number_input("Nhập b", value=0.0)
    c = st.number_input("Nhập c", value=0.0)

    if st.button("Giải"):
        if a == 0:
            if b == 0:
                st.write("⛔ Không phải phương trình.")
            else:
                st.write(f"✅ Nghiệm x = {-c / b:.2f}")
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                st.write("⛔ Vô nghiệm.")
            elif delta == 0:
                st.write(f"✅ Nghiệm kép x = {-b / (2*a):.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                st.write(f"✅ x1 = {x1:.2f}, x2 = {x2:.2f}")
