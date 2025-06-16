import streamlit as st
import pandas as pd

def run():
    st.header("📐 Load Reference (Eurocode 1)")

    st.subheader("⚙️ Dead Load (Permanent Actions)")

    dead_load_data = {
        "Ceramic tile": 200,
        "Granite (natural/artificial)": 2400,
        "Cement mortar (2–3 cm)": 500,
        "Waterproofing layer": 150,
        "Reinforced concrete slab (12 cm)": 3000,
    }

    material = st.selectbox("Select material", list(dead_load_data.keys()))
    unit_weight = dead_load_data[material]
    gamma_g = 1.35  # fixed by Eurocode

    st.write(f"🔹 Unit weight: **{unit_weight} kg/m²**")
    st.write(f"🔸 Eurocode γ<sub>G</sub> = {gamma_g}", unsafe_allow_html=True)
    st.success(f"✅ Design dead load = `{unit_weight * gamma_g:.2f} kg/m²`")

    st.markdown("---")
    st.subheader("🚶 Live Load (Variable Actions)")

    live_load_data = [
        {"Usage": "Residential (bedrooms, hotels, hospitals)", "qk": 2.0, "psi": 0.7},
        {"Usage": "Offices", "qk": 3.0, "psi": 0.7},
        {"Usage": "Classrooms, libraries, auditoriums", "qk": 4.0, "psi": 0.7},
        {"Usage": "Lobbies, assembly areas", "qk": 5.0, "psi": 0.7},
        {"Usage": "Storage/light industrial", "qk": 10.0, "psi": 0.6},
    ]

    df_live = pd.DataFrame(live_load_data)
    usage = st.selectbox("Select usage type", df_live["Usage"])
    row = df_live[df_live["Usage"] == usage].iloc[0]

    gamma_q = 1.5  # fixed by Eurocode
    design_q = row.qk * gamma_q

    st.write(f"🔹 Nominal live load q<sub>k</sub>: **{row.qk} kN/m²**", unsafe_allow_html=True)
    st.write(f"🔸 Eurocode γ<sub>Q</sub> = {gamma_q}", unsafe_allow_html=True)
    st.success(f"✅ Design live load = `{design_q:.2f} kN/m²`")
