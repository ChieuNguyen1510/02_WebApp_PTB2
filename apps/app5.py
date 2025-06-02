import streamlit as st
from datetime import date

def run():
    st.header("📅 Tính Số Ngày Giữa Hai Mốc")

    d1 = st.date_input("Ngày bắt đầu", value=date.today())
    d2 = st.date_input("Ngày kết thúc", value=date.today())

    if st.button("Tính số ngày"):
        days = abs((d2 - d1).days)
        st.write(f"✅ Khoảng cách: {days} ngày.")
        if d2 < d1:
            st.info("📌 Ngày kết thúc đang sớm hơn ngày bắt đầu.")
