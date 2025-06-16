import streamlit as st
import math
import pandas as pd

def phi_to_area(diameter):
    return math.pi * diameter**2 / 4

def run():
    st.header("🧮 Steel Reinforcement Area (Aₛ)")

    tab1, tab2, tab3 = st.tabs([
        "🔢 By Number of Bars", 
        "📏 By Spacing per Width", 
        "📚 Full Tables"
    ])

    # ========== TAB 1 ==========
    with tab1:
        st.subheader("🔢 Calculate Aₛ by Number of Bars")
        diameter = st.number_input("Bar diameter (mm)", min_value=6, max_value=36, value=16, step=1)
        quantity = st.number_input("Number of bars", min_value=1, value=4, step=1)

        area_single = phi_to_area(diameter)
        total_area = area_single * quantity

        st.write(f"🔹 Single bar area (mm²): `{area_single:.2f}`")
        st.success(f"✅ Total reinforcement area Aₛ = `{total_area:.2f}` mm²")

    # ========== TAB 2 ==========
    with tab2:
        st.subheader("📏 Calculate Aₛ by Bar Spacing")
        diameter = st.number_input("Bar diameter (mm)", min_value=6, max_value=36, value=16, step=1, key="dia2")
        spacing = st.number_input("Bar spacing (mm)", min_value=10, value=150, step=5)
        width = st.number_input("Width of beam/slab (mm)", min_value=100, value=1000, step=100)

        bars_per_width = width / spacing
        area_per_width = phi_to_area(diameter) * bars_per_width

        st.write(f"🔹 Bars per {width} mm: `{bars_per_width:.2f}`")
        st.success(f"✅ Reinforcement area Aₛ = `{area_per_width:.2f}` mm² per {width} mm")

    # ========== TAB 3 ==========
    with tab3:
        st.subheader("📚 Full Tables")

        diameters = list(range(6, 38, 2))  # 6 → 36 mm
        quantities = list(range(1, 15))    # 1 → 14 bars

        # BẢNG 1: A_s theo số thanh
        st.markdown("#### 🔢 Table 1: Aₛ by Number of Bars")
        df_bars = pd.DataFrame(columns=["Ø (mm)"] + [f"{i} bars" for i in quantities])
        for d in diameters:
            row = [d]
            for q in quantities:
                A = phi_to_area(d) * q
                row.append(round(A, 2))
            df_bars.loc[len(df_bars)] = row
        st.dataframe(df_bars.set_index("Ø (mm)"), use_container_width=True)

        # BẢNG 2: A_s/m theo spacing
        st.markdown("#### 📏 Table 2: Aₛ/m by Spacing")
        spacings = list(range(50, 301, 25))  # 50 → 300 mm
        df_spacing = pd.DataFrame(columns=["Ø (mm)"] + [f"{s} mm" for s in spacings])
        for d in diameters:
            row = [d]
            for s in spacings:
                A_per_m = phi_to_area(d) * (1000 / s)
                row.append(round(A_per_m, 2))
            df_spacing.loc[len(df_spacing)] = row
        st.dataframe(df_spacing.set_index("Ø (mm)"), use_container_width=True)
