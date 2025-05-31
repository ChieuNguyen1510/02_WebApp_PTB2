import streamlit as st
import math

# Tiêu đề trang
st.set_page_config(page_title="Giải PT bậc 2", layout="centered")

# Khởi tạo trạng thái đăng nhập nếu chưa có
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# =================== ĐĂNG NHẬP ===================
if not st.session_state["logged_in"]:
    st.title("🔐 Đăng nhập để sử dụng ứng dụng")

    with st.form("login_form"):
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")
        submitted = st.form_submit_button("Đăng nhập")

    if submitted:
        credentials = st.secrets["credentials"]
        if username in credentials and credentials[username] == password:
            st.success("✅ Đăng nhập thành công!")
            st.session_state["logged_in"] = True
        else:
            st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")

# =================== ỨNG DỤNG CHÍNH ===================
if st.session_state["logged_in"]:
    st.title("📐 Giải Phương Trình Bậc 2")

    a = st.number_input("Nhập a", value=1.0)
    b = st.number_input("Nhập b", value=0.0)
    c = st.number_input("Nhập c", value=0.0)

    if st.button("Giải"):
        if a == 0:
            if b == 0:
                st.write("⛔ Không phải phương trình.")
            else:
                x = -c / b
                st.write(f"✅ Nghiệm x = {x:.2f}")
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                st.write("⛔ Phương trình vô nghiệm.")
            elif delta == 0:
                x = -b / (2*a)
                st.write(f"✅ Nghiệm kép x = {x:.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                st.write(f"✅ Nghiệm x1 = {x1:.2f}, x2 = {x2:.2f}")

    # Thêm nút đăng xuất
    if st.button("Đăng xuất"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
