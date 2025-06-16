import streamlit as st
import pandas as pd
import math
from io import BytesIO

def calc_shear_stud(d, h, fck, fu, n):
    α = 1.0
    PRd1 = 0.29 * α * (d**2) * (fck**0.5) / 1e3  # kN
    PRd2 = 0.8 * fu * (math.pi * d**2 / 4) / 1e3  # kN
    PRd = min(PRd1, PRd2)
    total_capacity = PRd * n
    return PRd1, PRd2, PRd, total_capacity

def run():
    st.title("🔩 Shear Stud Design (EN 1994-1-1)")

    st.markdown("### 📥 Input Parameters")
    col1, col2 = st.columns(2)

    with col1:
        d = st.selectbox("Stud diameter d (mm)", [13, 16, 19, 22, 25], index=2)
        h = st.number_input("Stud height h (mm)", value=100.0, min_value=4*d*1.0)
        fck = st.selectbox("Concrete grade fck (MPa)", [20, 25, 30, 35, 40, 45, 50], index=2)
    with col2:
        fu = st.number_input("Stud ultimate strength fu (MPa)", value=450)
        n = st.number_input("Number of studs", value=10, step=1, min_value=1)

    if st.button("🧮 Calculate"):
        PRd1, PRd2, PRd, total = calc_shear_stud(d, h, fck, fu, n)

        st.markdown("### 📐 Design Formulas")
        st.latex(r"P_{Rd1} = 0.29 \cdot \alpha \cdot d^2 \cdot \sqrt{f_{ck}} \quad \text{(Concrete controlled)}")
        st.latex(r"P_{Rd2} = 0.8 \cdot f_u \cdot \frac{\pi d^2}{4} \quad \text{(Stud material controlled)}")
        st.markdown("- Where:")
        st.markdown("  - \( \alpha = 1.0 \) (recommended in EN 1994-1-1)")
        st.markdown("  - d: stud diameter in mm")
        st.markdown("  - \( f_{ck} \): characteristic compressive strength of concrete (MPa)")
        st.markdown("  - \( f_u \): ultimate tensile strength of stud (MPa)")

        st.markdown("### ✅ Results")
        st.write(f"🔹 PRd1 (by concrete): `{PRd1:.2f} kN`")
        st.write(f"🔹 PRd2 (by stud material): `{PRd2:.2f} kN`")
        st.write(f"🔸 Governing capacity per stud: `{PRd:.2f} kN`")
        st.write(f"🔸 Total capacity for {n} studs: `{total:.2f} kN`")

        # Export to Excel
        df = pd.DataFrame({
            "Stud Ø [mm]": [d],
            "Height [mm]": [h],
            "fck [MPa]": [fck],
            "fu [MPa]": [fu],
            "PRd1 [kN]": [PRd1],
            "PRd2 [kN]": [PRd2],
            "PRd Governing [kN]": [PRd],
            "Studs count": [n],
            "Total capacity [kN]": [total]
        })

        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Shear Stud")
            # No need for writer.save(); the 'with' block handles it
        st.download_button(
            "⬇️ Download Excel",
            buffer.getvalue(),
            file_name="shear_stud_design.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    run()