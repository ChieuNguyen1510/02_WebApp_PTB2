import streamlit as st

def run():
    st.header("⚖️ Tính Chỉ Số BMI")

    weight = st.number_input("Nhập cân nặng (kg)", value=0.0)
    height = st.number_input("Nhập chiều cao (m)", value=0.0)

    if st.button("Tính BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.write(f"✅ Chỉ số BMI = {bmi:.2f}")

            if bmi < 18.5:
                st.info("🔎 Bạn đang thiếu cân.")
            elif bmi < 24.9:
                st.success("👍 Cân nặng bình thường.")
            elif bmi < 29.9:
                st.warning("⚠️ Hơi thừa cân.")
            else:
                st.error("❗ Béo phì.")
        else:
            st.warning("⛔ Chiều cao phải lớn hơn 0.")
