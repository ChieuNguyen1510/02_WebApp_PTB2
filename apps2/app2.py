import streamlit as st

def run():
    st.header("📏 Tính Diện Tích Tam Giác")
    a = st.number_input("Nhập chiều dài cạnh đáy (a)", value=0.0)
    h = st.number_input("Nhập chiều cao (h)", value=0.0)

    if st.button("Tính diện tích"):
        if a > 0 and h > 0:
            area = 0.5 * a * h
            st.write(f"✅ Diện tích tam giác = {area:.2f}")
        else:
            st.warning("⛔ Vui lòng nhập số lớn hơn 0 cho cả a và h.")
