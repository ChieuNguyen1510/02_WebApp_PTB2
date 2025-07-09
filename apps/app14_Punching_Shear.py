import streamlit as st
import math

# ========== Hàm tính toán ==========
def punching_shear_check(d, column_x, column_y, V_ed, f_ck):
    # Tham số vật liệu và hệ số
    f_cd = f_ck / 1.5  # MPa
    k = min(1 + math.sqrt(200 / d), 2.0)  # theo EC2
    v_rd_c = 0.18 * k * (f_cd)**(2/3)  # MPa

    # Chu vi kiểm tra u = chu vi tại khoảng cách d quanh cột
    u = 2 * (column_x + column_y + 2 * math.pi * d)  # mm
    A = u * d  # diện tích cắt (mm^2)
    V_rd = v_rd_c * A / 1e3  # đổi sang kN

    # Kiểm tra
    status = "✅ Safe" if V_ed <= V_rd else "❌ Unsafe"
    return V_rd, status, k, v_rd_c, A

# ========== Giao diện ==========
def run():
    st.title("🕳️ Slab Punching Shear Check")

    st.markdown("Enter slab and column properties:")
    d = st.number_input("Effective Depth d (mm)", value=180.0)
    column_x = st.number_input("Column Width x (mm)", value=400.0)
    column_y = st.number_input("Column Width y (mm)", value=400.0)
    V_ed = st.number_input("Design Shear Force Vₑₓ (kN)", value=450.0)
    f_ck = st.number_input("Concrete Grade fₐₚ (MPa)", value=30.0)

    if st.button("🔍 Check Punching Shear"):
        V_rd, status, k, v_rd_c, A = punching_shear_check(d, column_x, column_y, V_ed, f_ck)

        st.markdown("### ✅ Result")
        st.write(f"Design punching shear resistance **V<sub>Rd</sub> = {V_rd:.2f} kN**", unsafe_allow_html=True)
        st.write(f"Status: {status}")

        # Hiển thị công thức
        st.markdown("---")
        st.markdown("### 📘 Calculation Explanation")
        st.latex(r"k = \min\left(1 + \sqrt{\frac{200}{d}}, 2.0\right) = %.2f" % k)
        st.latex(r"v_{Rd,c} = 0.18 \cdot k \cdot f_{cd}^{2/3} = %.2f\ \text{MPa}" % v_rd_c)
        st.latex(r"u = 2(x + y + 2\pi d) = %.0f\ \text{mm}" % (2 * (column_x + column_y + 2 * math.pi * d)))
        st.latex(r"A = u \cdot d = %.0f\ \text{mm}^2" % A)
        st.latex(r"V_{Rd} = v_{Rd,c} \cdot A = %.2f\ \text{kN}" % V_rd)

# if __name__ == "__main__":
#     run()
