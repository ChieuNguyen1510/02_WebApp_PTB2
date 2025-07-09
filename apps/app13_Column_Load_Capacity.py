import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def calculate_column_capacity(b, h, As, fc, fy, P, M):
    # Constants (ACI 318 simplified)
    phi = 0.65  # Strength reduction factor for compression
    gamma_c = 0.85  # Factor for concrete strength

    # Gross area and section modulus
    Ag = b * h / 10**6  # mm² to m²
    Ig = (b * h**3) / 12 / 10**12  # mm⁴ to m⁴
    d = h - 50  # Approximate effective depth (assuming 50mm cover)

    # Nominal axial capacity (P0)
    P0 = 0.85 * fc * Ag + fy * As / 10**3  # N to kN

    # Interaction diagram (simplified P-M curve)
    P_u = phi * P0  # Design axial capacity
    M_u_max = P_u * (h / 2000)  # Approximate max moment due to eccentricity (h/2)

    # Check if load is within capacity
    if P <= P_u and M <= M_u_max:
        status = "✅ Safe"
    else:
        status = "❌ Unsafe"

    return P_u, M_u_max, status

def plot_pm_interaction(P_u, M_u_max, P, M):
    fig, ax = plt.subplots()
    P_values = np.linspace(0, P_u, 100)
    M_values = P_values * (h / 2000)  # Linear approximation
    ax.plot(M_values, P_values, label="P-M Interaction Curve")
    ax.plot(M, P, 'ro', label="Applied Load")
    ax.set_xlabel("Moment (kNm)")
    ax.set_ylabel("Axial Load (kN)")
    ax.set_title("P-M Interaction Diagram")
    ax.legend()
    ax.grid(True)
    return fig

def run():
    st.title("🌇 Column Load Capacity Checker")

    st.markdown("Enter column and material properties (in mm and MPa):")
    
    b = st.number_input("Width (b, mm)", value=300.0, min_value=100.0)
    h = st.number_input("Height (h, mm)", value=500.0, min_value=100.0)
    As = st.number_input("Reinforcement Area (As, mm²)", value=1200.0, min_value=100.0)
    fc = st.number_input("Concrete Strength (f'_c, MPa)", value=25.0, min_value=20.0)
    fy = st.number_input("Steel Yield Strength (f_y, MPa)", value=400.0, min_value=200.0)
    P = st.number_input("Applied Axial Load (P, kN)", value=1000.0, min_value=0.0)
    M = st.number_input("Applied Moment (M, kNm)", value=50.0, min_value=0.0)

    if st.button("Calculate"):
        P_u, M_u_max, status = calculate_column_capacity(b, h, As, fc, fy, P, M)
        
        st.markdown("### ✅ Results")
        st.write(f"Design Axial Capacity (P_u): {P_u:.2f} kN")
        st.write(f"Max Allowable Moment (M_u_max): {M_u_max:.2f} kNm")
        st.write(f"Status: {status}")

        fig = plot_pm_interaction(P_u, M_u_max, P, M)
        st.pyplot(fig)

        # Export to Excel
        st.markdown("---")
        st.markdown("📤 Export Result")
        df = pd.DataFrame({
            "Parameter": ["Width", "Height", "Reinforcement Area", "Concrete Strength", "Steel Yield Strength", "Applied Axial Load", "Applied Moment", "Design Axial Capacity", "Max Allowable Moment", "Status"],
            "Value": [b, h, As, fc, fy, P, M, P_u, M_u_max, status],
            "Unit": ["mm", "mm", "mm²", "MPa", "MPa", "kN", "kNm", "kN", "kNm", ""]
        })

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="ColumnCapacity")
        st.download_button("📥 Download file", data=output.getvalue(), file_name="column_capacity.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    run()