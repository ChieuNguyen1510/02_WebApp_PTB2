import streamlit as st
import pandas as pd

def run():
    st.header("📦 Load Reference Table")

    st.subheader("⚙️ Dead Load (Tĩnh tải)")

    dead_load_data = {
        "Lớp gạch ceramic lát sàn": 200,
        "Lớp granite thiên nhiên, nhân tạo": 2400,
        "Vữa xi măng lát nền (2-3cm)": 500,
        "Lớp chống thấm, keo dán gạch": 150,
        "Lớp bê tông cốt thép sàn (d=12cm)": 3000,
    }

    material = st.selectbox("Select material", list(dead_load_data.keys()))
    unit_weight = dead_load_data[material]
    overload_factor = st.number_input("Overload factor (γ)", value=1.1)

    st.write(f"🔹 Unit weight: **{unit_weight} kg/m²**")
    st.write(f"🔹 Design load: **{unit_weight * overload_factor:.2f} kg/m²**")

    st.markdown("---")
    st.subheader("🚶 Live Load (Hoạt tải)")

    live_load_data = [
        {"Type": "Phòng ngủ, khách sạn, bệnh viện, trại giam", "Full": 200, "Sustained": 70},
        {"Type": "Văn phòng", "Full": 300, "Sustained": 100},
        {"Type": "Lớp học, thư viện, hội trường", "Full": 400, "Sustained": 120},
        {"Type": "Sảnh, khu công cộng", "Full": 500, "Sustained": 150},
        {"Type": "Kho nhẹ, gara", "Full": 1000, "Sustained": 300},
    ]

    df_live = pd.DataFrame(live_load_data)
    selected_type = st.selectbox("Usage type", df_live["Type"])
    selected_row = df_live[df_live["Type"] == selected_type].iloc[0]

    st.write(f"🔹 Full live load: **{selected_row['Full']} kg/m²**")
    st.write(f"🔹 Sustained live load: **{selected_row['Sustained']} kg/m²**")
