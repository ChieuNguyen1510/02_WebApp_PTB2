import streamlit as st
from apps import app1, app2, app3, app4, app5

st.set_page_config(page_title="General Application", layout="centered")

# Danh sách apps
apps = {
    "Convert Unit": app1.run,
    "Concrete strength": app2.run,
    "Steel strength": app3.run,
    "Reinforcement area": app4.run,
    "Loading": app5.run
}

# Giao diện lựa chọn
st.title("📱 General Application")
choice = st.selectbox("Select the application you want to use:", list(apps.keys()))
apps[choice]()  # Gọi app tương ứng
