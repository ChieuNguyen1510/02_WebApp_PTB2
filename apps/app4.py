import streamlit as st
import math

def phi_to_area(diameter):
    return math.pi * diameter**2 / 4

def run():
    st.header("🧮 Steel Reinforcement Area Calculator")

    tab1, tab2 = st.tabs(["🔢 By Number of Bars", "📏 By Spacing per Meter"])

    # ========== TAB 1: Theo số thanh ==========
    with tab1:
        st.subheader("🔢 Total Area by Number of Bars")

        diameter = st.number_input("Bar diameter (mm)", min_value=6, max_value=40, value=16, step=1)
        quantity = st.number_input("Number of bars", min_value=1, value=4, step=1)

        area_single = phi_to_area(diameter)
        total_area = area_single * quantity

        st.write(f"🔹 Area of one bar (mm²): `{area_single:.2f}`")
        st.success(f"✅ Total reinforcement area Aₛ = `{total_area:.2f}` mm²")

    # ========== TAB 2: Theo khoảng cách ==========
    with tab2:
        st.subheader("📏 Area per Meter by Spacing")

        diameter = st.number_input("Bar diameter (mm)", min_value=6, max_value=40, value=16, step=1, key="dia_spacing")
        spacing = st.number_input("Bar spacing (mm)", min_value=10, value=150, step=5)
        width = st.number_input("Width of beam/slab (mm)", min_value=100, value=1000, step=100)

        bars_per_meter = width / spacing
        area_per_meter = phi_to_area(diameter) * bars_per_meter

        st.write(f"🔹 Bars per {width} mm: `{bars_per_meter:.2f}`")
        st.success(f"✅ Aₛ ≈ `{area_per_meter:.2f}` mm² per {width} mm width")
