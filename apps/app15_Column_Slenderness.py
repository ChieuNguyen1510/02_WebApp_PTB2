import streamlit as st
import pandas as pd
from io import BytesIO

# Eurocode và TCVN các hệ số khuyến nghị
standards = {
    "Eurocode 2": {
        "lambda_lim": 90,
    },
    "TCVN 5574:2018": {
        "lambda_lim": 70,
    }
}

boundary_factors = {
    "Pinned - Pinned": 1.0,
    "Fixed - Free": 2.0,
    "Fixed - Fixed": 0.7,
    "Pinned - Fixed": 0.8,
    "Free - Free": 2.1
}

def run():
    st.title("📏 Column Slenderness Check")

    # ===== Chọn tiêu chuẩn =====
    code = st.selectbox("Select design standard:", list(standards.keys()))
    lambda_lim = standards[code]["lambda_lim"]

    st.markdown("### 🔧 Input Parameters")
    L_actual = st.number_input("Actual Length of Column L_actual (mm)", value=3000.0, min_value=100.0)
    bc = st.selectbox("Boundary Condition (for effective length estimation):", list(boundary_factors.keys()))
    b = st.number_input("Width of Column Section b (mm)", value=300.0, min_value=50.0)
    h = st.number_input("Height of Column Section h (mm)", value=500.0, min_value=50.0)

    # ===== Tính toán =====
    L = L_actual * boundary_factors[bc]
    I = (b * h**3) / 12  # mm^4
    A = b * h  # mm^2
    r = (I / A) ** 0.5  # mm

    if st.button("Check Slenderness"):
        lambda_val = L / r

        st.markdown("### 📊 Results")
        st.write(f"Effective Length (L) = **{L:.2f} mm**")
        st.write(f"Radius of Gyration (r) = **{r:.2f} mm**")
        st.write(f"Slenderness ratio λ = **{lambda_val:.2f}**")
        st.write(f"Limit value λ<sub>lim</sub> = **{lambda_lim}** ({code})", unsafe_allow_html=True)

        if lambda_val <= lambda_lim:
            st.success("✅ The column is considered **short (non-slender)**.")
        else:
            st.error("❌ The column is considered **slender**, second-order effects should be considered.")

        # Export kết quả ra Excel
        df = pd.DataFrame({
            "Parameter": ["Actual Length", "Boundary Factor", "Effective Length", "Section Width", "Section Height", "Radius of Gyration", "λ", "λ_lim", "Status"],
            "Value": [L_actual, boundary_factors[bc], L, b, h, r, lambda_val, lambda_lim, "Short" if lambda_val <= lambda_lim else "Slender"],
            "Unit": ["mm", "-", "mm", "mm", "mm", "mm", "-", "-", ""]
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
