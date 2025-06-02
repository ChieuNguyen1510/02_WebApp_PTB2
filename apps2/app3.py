import streamlit as st

def run():
    st.header("🌡️ Chuyển Đổi Nhiệt Độ C ↔ F")

    option = st.radio("Chọn chiều chuyển đổi:", ["C → F", "F → C"])
    value = st.number_input("Nhập giá trị nhiệt độ", value=0.0)

    if st.button("Chuyển đổi"):
        if option == "C → F":
            result = value * 9/5 + 32
            st.write(f"✅ {value:.1f}°C = {result:.1f}°F")
        else:
            result = (value - 32) * 5/9
            st.write(f"✅ {value:.1f}°F = {result:.1f}°C")
