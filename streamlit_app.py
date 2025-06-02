import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Danh sách apps
apps = {
    "Convert Unit": app1.run,
    "Tính diện tích tam giác": app2.run,
    "Chuyển đổi độ C ↔ F": app3.run,
    "Tính BMI": app4.run,
    "Số ngày giữa 2 mốc": app5.run
}

# Giao diện lựa chọn
st.title("📱 General Application")
choice = st.selectbox("Select the application you want to use:", list(apps.keys()))
apps[choice]()  # Gọi app tương ứng
