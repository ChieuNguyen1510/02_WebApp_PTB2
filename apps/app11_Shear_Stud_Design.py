import streamlit as st
import pandas as pd
from io import BytesIO

def run():
    st.title("🛠️ Shear Stud Design (EN 1994-1-1)")

    st.markdown("This tool calculates the shear resistance of headed studs based on Eurocode 4 (EN 1994-1-1).")

    # Inputs
    st.header("🔢 Input Parameters")

    col1, col2 = st.columns(2)
    with col1:
        stud_diameter = st.number_input("Stud Diameter d (mm)", value=19)
        fu = st.number_input("Ultimate Tensile Strength of Stud (fu) [MPa]", value=450)
        As = 3.1416 * stud_diameter**2 / 4  # mm²
        fck = st.number_input("Characteristic Concrete Strength fck [MPa]", value=30)

    with col2:
        h_ef = st.number_input("Effective Height hef (mm)", value=100)
        gamma_v = st.number_input("Partial Factor γv", value=1.25)
        density = st.number_input("Density of Concrete ρ (kg/m³)", value=2500)

    # Calculations
    st.header("🧮 Results")

    # Eurocode 4: Clause 6.6.3.1
    V1 = 0.8 * fu * As / gamma_v
    V2 = 0.29 * (3.1416 * stud_diameter**2 / 4) * (density / 2200)**0.5 * (fck**0.5) / gamma_v
    Vrd = min(V1, V2)  # N

    st.metric("Stud cross-section area Aₛ", f"{As:.2f} mm²")
    st.metric("Shear resistance V₁ (governed by steel)", f"{V1/1000:.2f} kN")
    st.metric("Shear resistance V₂ (governed by concrete)", f"{V2/1000:.2f} kN")
    st.success(f"✅ Design shear resistance V<sub>Rd</sub>: **{Vrd/1000:.2f} kN**", unsafe_allow_html=True)

    st.markdown("---")
    st.header("📘 Formulas Used")

    st.latex(r"A_s = \frac{\pi d^2}{4}")
    st.latex(r"V_{1} = \frac{0.8 f_u A_s}{\gamma_v}")
    st.latex(r"V_{2} = \frac{0.29 \cdot \pi d^2 / 4 \cdot \sqrt{\rho/2200} \cdot \sqrt{f_{ck}}}{\gamma_v}")
    st.latex(r"V_{Rd} = \min(V_1, V_2)")

    # Export to Excel
    df = pd.DataFrame([{
        "Stud Diameter (mm)": stud_diameter,
        "fu (MPa)": fu,
        "As (mm²)": round(As, 2),
        "Concrete fck (MPa)": fck,
        "Density (kg/m³)": density,
        "hef (mm)": h_ef,
        "γv": gamma_v,
        "V1 (kN)": round(V1/1000, 2),
        "V2 (kN)": round(V2/1000, 2),
        "Design Vrd (kN)": round(Vrd/1000, 2)
    }])

    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Shear Stud")
    buffer.seek(0)

    st.download_button(
        label="⬇️ Download Excel",
        data=buffer,
        file_name="shear_stud_design.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
