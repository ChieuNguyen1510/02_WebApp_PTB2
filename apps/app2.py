import streamlit as st
import pandas as pd

def run():
    st.header("📋 Concrete Strength Table (Eurocode 2)")

    # Concrete data according to EC2
    data = [
        {"Grade": "C20/25", "fck": 20, "fcm": 28, "fctm": 2.2, "fctk,0.05": 1.6, "fctk,0.95": 2.8, "Ecm": 30_000},
        {"Grade": "C25/30", "fck": 25, "fcm": 33, "fctm": 2.6, "fctk,0.05": 1.9, "fctk,0.95": 3.3, "Ecm": 31_000},
        {"Grade": "C30/37", "fck": 30, "fcm": 38, "fctm": 2.9, "fctk,0.05": 2.1, "fctk,0.95": 3.6, "Ecm": 32_000},
        {"Grade": "C35/45", "fck": 35, "fcm": 43, "fctm": 3.2, "fctk,0.05": 2.3, "fctk,0.95": 4.1, "Ecm": 34_000},
        {"Grade": "C40/50", "fck": 40, "fcm": 48, "fctm": 3.5, "fctk,0.05": 2.5, "fctk,0.95": 4.4, "Ecm": 35_000},
        {"Grade": "C45/55", "fck": 45, "fcm": 53, "fctm": 3.8, "fctk,0.05": 2.7, "fctk,0.95": 4.9, "Ecm": 36_000},
        {"Grade": "C50/60", "fck": 50, "fcm": 58, "fctm": 4.1, "fctk,0.05": 2.9, "fctk,0.95": 5.3, "Ecm": 37_000},
    ]
    df = pd.DataFrame(data)

    # Grade selector
    grade = st.selectbox("Select concrete grade:", df["Grade"])

    selected = df[df["Grade"] == grade].iloc[0]

    st.markdown("### ✅ Concrete properties:")
    st.write(f"**f<sub>ck</sub>** (Characteristic compressive strength, MPa): `{selected.fck}`", unsafe_allow_html=True)
    st.write(f"**f<sub>cm</sub>** (Mean compressive strength, MPa): `{selected.fcm}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctm</sub>** (Mean tensile strength, MPa): `{selected.fctm}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctk,0.05</sub>** (5% fractile tensile strength, MPa): `{selected['fctk,0.05']}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctk,0.95</sub>** (95% fractile tensile strength, MPa): `{selected['fctk,0.95']}`", unsafe_allow_html=True)
    st.write(f"**E<sub>cm</sub>** (Modulus of elasticity, MPa): `{selected.Ecm}`", unsafe_allow_html=True)

    with st.expander("📘 Reference"):
        st.markdown("Data from **EN 1992-1-1 (Eurocode 2)**, section 3.1.2")
