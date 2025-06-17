import streamlit as st
import pandas as pd
from io import BytesIO

def run():
    st.title("🔩 Shear Stud Design (EN1994-1-1)")

    st.markdown("Enter stud and material properties:")

    d = st.number_input("Stud diameter d (mm)", value=19.0, min_value=10.0)
    fu = st.number_input("Ultimate strength of stud fu (MPa)", value=450.0, min_value=100.0)
    As = 3.1416 * (d / 2)**2  # Cross-sectional area of one stud in mm²
    gammaV = 1.25

    # Prd calculation (Eurocode 4 - 6.6.3.1)
    Prd = 0.8 * fu * As / gammaV

    # Hiển thị công thức và kết quả
    st.markdown("### ✅ Shear Resistance Calculation")
    st.markdown(f"""
    - Cross-sectional area of stud:  
      $$
      A_s = \\frac{{\\pi \\times d^2}}{{4}} = \\frac{{3.1416 \\times {d}^2}}{{4}} = {As:.1f}\\ \\text{{mm}}^2
      $$

    - Design shear resistance:  
      $$
      V_{{Rd}} = \\frac{{0.8 \\times f_u \\times A_s}}{{\\gamma_V}} = 
      \\frac{{0.8 \\times {fu} \\times {As:.1f}}}{{{gammaV}}} = {Prd:.1f}\\ \\text{{N}} = {Prd/1000:.2f}\\ \\text{{kN}}
      $$
    """, unsafe_allow_html=True)

    st.success(f"✅ V₍Rd₎ = **{Prd / 1000:.2f} kN**")

    # Thêm chú thích
    st.markdown("""
    **Where:**
    - γ_V is the partial factor;
    - d is the diameter of the shank of the stud, 16 mm ≤ d ≤ 25 mm;
    - f_u is the specified ultimate tensile strength of the material of the stud but not greater than 500 N/mm²;
    **Note:** The value for γ_V may be given in the National Annex. The recommended value for γ_V is 1.25.
    """)

    # Export to Excel
    st.markdown("---")
    st.markdown("📤 Export Result")
    if st.button("Download Excel"):
        df = pd.DataFrame({
            "Parameter": ["Stud diameter (d)", "fu", "As", "Prd"],
            "Value": [d, fu, As, Prd],
            "Unit": ["mm", "MPa", "mm²", "N"]
        })

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="ShearStud")
        st.download_button("📥 Download file", data=output.getvalue(), file_name="shear_stud_design.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")