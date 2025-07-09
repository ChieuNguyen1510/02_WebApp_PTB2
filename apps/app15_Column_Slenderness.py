import streamlit as st
import pandas as pd
from io import BytesIO

# Eurocode và TCVN các hệ số khuyến nghị
standards = {
    "Eurocode 2": {
        "lambda_lim": 90,  # Giới hạn độ mảnh với cột chịu nén đồng tâm
    },
    "TCVN 5574:2018": {
        "lambda_lim": 70,  # Hệ số giới hạn độ mảnh với cột chịu nén
    }
}

def run():
    st.title("📏 Column Slenderness Check")

    # ===== Chọn tiêu chuẩn =====
    code = st.selectbox("Select design standard:", list(standards.keys()))
    lambda_lim = standards[code]["lambda_lim"]

    st.markdown("### 🔧 Input Parameters")
    L = st.number_input("Effective Length L (mm)", value=3000.0, min_value=100.0)
    r = st.number_input("Radius of Gyration r (mm)", value=50.0, min_value=1.0)

    # ===== Điều kiện biên minh họa =====
    st.markdown("""
    #### 🔒 Boundary Conditions (for estimating L)
    - **Pinned - Pinned**: L = actual length
    - **Fixed - Free**: L = 2 × actual length
    - **Fixed - Fixed**: L = 0.7 × actual length
    """)

    if st.button("Check Slenderness"):
        lambda_val = L / r

        st.markdown("### 📊 Results")
        st.write(f"Slenderness ratio λ = **{lambda_val:.2f}**")
        st.write(f"Limit value λ<sub>lim</sub> = **{lambda_lim}** ({code})", unsafe_allow_html=True)

        if lambda_val <= lambda_lim:
            st.success("✅ The column is considered **short (non-slender)**.")
        else:
            st.error("❌ The column is considered **slender**, second-order effects should be considered.")

        # Export kết quả ra Excel
        df = pd.DataFrame({
            "Parameter": ["Effective Length", "Radius of Gyration", "λ", "λ_lim", "Status"],
            "Value": [L, r, lambda_val, lambda_lim, "Short" if lambda_val <= lambda_lim else "Slender"],
            "Unit": ["mm", "mm", "-", "-", ""]
        })

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Slenderness Check")

        st.download_button(
            "📥 Download Excel Report",
            data=output.getvalue(),
            file_name="column_slenderness_check.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == '__main__':
    run()
