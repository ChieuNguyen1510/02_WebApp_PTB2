import streamlit as st
import pandas as pd

def run():
    st.header("🔩 Steel Strength Lookup")

    tab1, tab2 = st.tabs(["🟦 Steel Plates", "🟥 Rebars"])

    # ========== TAB 1: THÉP TẤM ==========
    with tab1:
        st.subheader("🟦 Steel Plates")

        data_plate = [
            {"Grade": "S235", "fy": 235, "fu": 360, "Standard": "EN 10025"},
            {"Grade": "S275", "fy": 275, "fu": 410, "Standard": "EN 10025"},
            {"Grade": "S355", "fy": 355, "fu": 510, "Standard": "EN 10025"},
            {"Grade": "A36",  "fy": 250, "fu": 400, "Standard": "ASTM A36"},
            {"Grade": "Q235", "fy": 235, "fu": 375, "Standard": "GB/T 700"},
            {"Grade": "Q345", "fy": 345, "fu": 470, "Standard": "GB/T 1591"},
        ]
        df_plate = pd.DataFrame(data_plate)

        grade = st.selectbox("Select plate steel grade:", df_plate["Grade"], key="plate_grade")
        selected = df_plate[df_plate["Grade"] == grade].iloc[0]

        st.markdown("### ✅ Steel Properties (Plate):")
        st.write(f"**Standard:** {selected.Standard}")
        st.write(f"**Yield strength f<sub>y</sub>** (MPa): `{selected.fy}`", unsafe_allow_html=True)
        st.write(f"**Ultimate strength f<sub>u</sub>** (MPa): `{selected.fu}`", unsafe_allow_html=True)

    # ========== TAB 2: THÉP TRÒN ==========
    with tab2:
        st.subheader("🟥 Reinforcement Bars (Rebars)")

        data_rebar = [
            {"Grade": "SD295", "fyk": 295, "ftk": 440, "Es": 200000, "Standard": "JIS G3112"},
            {"Grade": "SD390", "fyk": 390, "ftk": 600, "Es": 200000, "Standard": "JIS G3112"},
            {"Grade": "CB240", "fyk": 240, "ftk": 380, "Es": 200000, "Standard": "TCVN 1651-1"},
            {"Grade": "CB300", "fyk": 300, "ftk": 500, "Es": 200000, "Standard": "TCVN 1651-1"},
            {"Grade": "CB400-V", "fyk": 400, "ftk": 570, "Es": 200000, "Standard": "TCVN 1651-2"},
            {"Grade": "CB500-V", "fyk": 500, "ftk": 630, "Es": 200000, "Standard": "TCVN 1651-2"},
            {"Grade": "B500B", "fyk": 500, "ftk": 540, "Es": 200000, "Standard": "EN 1992-1-1 / EN 10080"},
        ]
        df_rebar = pd.DataFrame(data_rebar)

        grade = st.selectbox("Select rebar grade:", df_rebar["Grade"], key="rebar_grade")
        selected = df_rebar[df_rebar["Grade"] == grade].iloc[0]

        st.markdown("### ✅ Steel Properties (Rebar):")
        st.write(f"**Standard:** {selected.Standard}")
        st.write(f"**Yield strength f<sub>yk</sub>** (MPa): `{selected.fyk}`", unsafe_allow_html=True)
        st.write(f"**Ultimate strength f<sub>tk</sub>** (MPa): `{selected.ftk}`", unsafe_allow_html=True)
        st.write(f"**Modulus of elasticity E<sub>s</sub>** (MPa): `{selected.Es}`", unsafe_allow_html=True)

        with st.expander("📘 Notes"):
            st.markdown("""
            - **B500B** is the most common grade in Eurocode.
            - It is defined in **EN 1992-1-1** and **EN 10080**.
            - The design yield strength is typically 500 MPa.
            """)
