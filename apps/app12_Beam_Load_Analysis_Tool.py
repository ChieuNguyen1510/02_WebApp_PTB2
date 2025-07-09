import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def calculate_beam(length, uniform_load, point_load, point_pos, E, I):
    # Max Moment (kNm)
    max_moment = (uniform_load * length**2 / 8) + (point_load * (length - point_pos)) if 0 <= point_pos <= length else (uniform_load * length**2 / 8)
    
    # Max Shear (kN)
    max_shear = (uniform_load * length / 2) + point_load
    
    # Deflection (m) - Using E and I
    deflection = (uniform_load * length**4 / (384 * E * I)) + (point_load * point_pos**2 * (length - point_pos)**2 / (3 * E * I * length))
    
    return max_moment, max_shear, deflection

def plot_beam(length, uniform_load, point_load, point_pos):
    x = np.linspace(0, length, 100)
    m = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] <= point_pos:
            m[i] = (uniform_load * x[i]**2 / 2) + (point_load * x[i] / length * (length - point_pos))
        else:
            m[i] = (uniform_load * x[i]**2 / 2) - (uniform_load * x[i] * (x[i] - length)) + (point_load * (x[i] - point_pos))
    plt.plot(x, m)
    plt.title("Bending Moment Diagram")
    plt.xlabel("Length (m)")
    plt.ylabel("Moment (kNm)")
    st.pyplot()

def run():
    st.title("🌉 Beam Load Analysis Tool")

    st.markdown("Enter beam and material properties:")
    
    length = st.number_input("Length (m)", value=5.0, min_value=0.1)
    uniform_load = st.number_input("Uniform Load (kN/m)", value=10.0, min_value=0.0)
    point_load = st.number_input("Point Load (kN)", value=5.0, min_value=0.0)
    point_pos = st.number_input("Point Load Position (m)", value=2.5, min_value=0.0, max_value=length)
    E = st.number_input("Elastic Modulus (GPa)", value=200.0, min_value=1.0) * 10**9  # Convert to Pa
    I = st.number_input("Moment of Inertia (m⁴)", value=0.0001, min_value=0.00001)

    if st.button("Calculate"):
        max_moment, max_shear, deflection = calculate_beam(length, uniform_load, point_load, point_pos, E, I)
        
        st.markdown("### ✅ Results")
        st.write(f"Max Moment: {max_moment:.2f} kNm")
        st.write(f"Max Shear: {max_shear:.2f} kN")
        st.write(f"Deflection: {deflection:.4f} m")
        
        plot_beam(length, uniform_load, point_load, point_pos)

        # Export to Excel
        st.markdown("---")
        st.markdown("📤 Export Result")
        df = pd.DataFrame({
            "Parameter": ["Length", "Uniform Load", "Point Load", "Point Position", "Max Moment", "Max Shear", "Deflection"],
            "Value": [length, uniform_load, point_load, point_pos, max_moment, max_shear, deflection],
            "Unit": ["m", "kN/m", "kN", "m", "kNm", "kN", "m"]
        })

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="BeamAnalysis")
        st.download_button("📥 Download file", data=output.getvalue(), file_name="beam_analysis.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    run()