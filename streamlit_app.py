import streamlit as st
import math

# Thiết lập giao diện
st.set_page_config(page_title="Ứng dụng Tổng hợp", layout="centered")

# Danh sách app con
def app1():
    st.header("📐 Giải Phương Trình Bậc 2")
    a = st.number_input("Nhập a", value=1.0, key="a1")
    b = st.number_input("Nhập b", value=0.0, key="b1")
    c = st.number_input("Nhập c", value=0.0, key="c1")
    if st.button("Giải", key="solve1"):
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

def app2():
    st.header("📏 Tính diện tích tam giác")
    a = st.number_input("Cạnh a", key="a2")
    h = st.number_input("Chiều cao h", key="h2")
    if st.button("Tính", key="calc2"):
        area = 0.5 * a * h
        st.write(f"✅ Diện tích = {area:.2f}")

def app3():
    st.header("🔄 Chuyển đổi độ C ↔ độ F")
    c = st.number_input("Nhập độ C", key="c3")
    if st.button("Chuyển", key="conv3"):
        f = c * 9/5 + 32
        st.write(f"✅ {c:.1f}°C = {f:.1f}°F")

def app4():
    st.header("⚖️ Tính BMI")
    weight = st.number_input("Cân nặng (kg)", key="w4")
    height = st.number_input("Chiều cao (m)", key="h4")
    if st.button("Tính BMI", key="bmi4") and height > 0:
        bmi = weight / height**2
        st.write(f"✅ BMI = {bmi:.2f}")

def app5():
    st.header("📅 Tính số ngày giữa hai ngày")
    d1 = st.date_input("Ngày bắt đầu", key="d5a")
    d2 = st.date_input("Ngày kết thúc", key="d5b")
    if st.button("Tính ngày", key="days5"):
        delta = abs((d2 - d1).days)
        st.write(f"✅ Số ngày: {delta} ngày")

# ========== Giao diện chính ==========
st.title("📱 Ứng Dụng Tổng Hợp")

app_names = ["Giải PT bậc 2", "Tính diện tích tam giác", "Chuyển đổi độ C↔F", "Tính BMI", "Số ngày giữa 2 mốc"]
app_funcs = [app1, app2, app3, app4, app5]

choice = st.selectbox("Chọn ứng dụng:", app_names)
app_funcs[app_names.index(choice)]()
