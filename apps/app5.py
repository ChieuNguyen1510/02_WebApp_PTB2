import streamlit as st
import pandas as pd

def run():
    st.header("📦 Load Reference Table")

    st.subheader("⚙️ Dead Load")

    dead_load_data = {
        "Ceramic tile layer": 200,
        "Granite (natural/artificial)": 2400,
        "Cement mortar (2–3 cm)": 500,
        "Waterproofing, tile adhesive layer": 150,
        "Reinforced concrete slab (12 cm)": 3000,
    }

    material = st.selectbox("Select material", list(dead_load_data.keys()))
    unit_weight = dead_load_data[material]
    overload_factor = st.number_input("Overload factor (γ)", value=1.1)

    st.write(f"🔹 Unit weight: **{unit_weight} kg/m²**")
    st.write(f"🔹 Design load: **{unit_weight * overload_factor:.2f} kg/m²**")

    st.markdown("---")
    st.subheader("🚶 Live Load")

    live_load_data = [
        {"Type": "Bedrooms, hotels, hospitals, prisons", "Full": 200, "Sustained": 70},
        {"Type": "Offices", "Full": 300, "Sustained": 100},
        {"Type": "Classrooms, libraries, auditoriums", "Full": 400, "Sustained": 120},
        {"Type": "Lobbies, public spaces", "Full": 500, "Sustained": 150},
        {"Type": "Light warehouses, garages", "Full": 1000, "Sustained": 300},
    ]

    df_live = pd.DataFrame(live_load_data)
    selected_type = st.selectbox("Select usage type", df_live["Type"])
    selected_row = df_live[df_live["Type"] == selected_type].iloc[0]

    st.write(f"🔹 Full live load: **{selected_row['Full']} kg/m²**")
    st.write(f"🔹 Sustained live load: **{selected_row['Sustained']} kg/m²**")
