import streamlit as st
import pandas as pd

def run():
    st.header("📋 Concrete Strength Table")

    tab1, tab2 = st.tabs(["🇪🇺 Eurocode 2", "🇨🇳 Chinese Standard (GB50010)"])

    # ========== TAB 1: EUROCODE ==========
    with tab1:
        st.subheader("🟦 Eurocode 2 (EN 1992-1-1)")

        ec2_data = [
            {"Grade": "C20/25", "fck": 20, "fcm": 28, "fctm": 2.2, "fctk,0.05": 1.6, "fctk,0.95": 2.8, "Ecm": 30000},
            {"Grade": "C25/30", "fck": 25, "fcm": 33, "fctm": 2.6, "fctk,0.05": 1.9, "fctk,0.95": 3.3, "Ecm": 31000},
            {"Grade": "C30/37", "fck": 30, "fcm": 38, "fctm": 2.9, "fctk,0.05": 2.1, "fctk,0.95": 3.6, "Ecm": 32000},
            {"Grade": "C32/40", "fck": 32, "fcm": 40, "fctm": 3.05, "fctk,0.05": 2.2, "fctk,0.95": 3.8, "Ecm": 33000},
            {"Grade": "C35/45", "fck": 35, "fcm": 43, "fctm": 3.2, "fctk,0.05": 2.3, "fctk,0.95": 4.1, "Ecm": 34000},
            {"Grade": "C40/50", "fck": 40, "fcm": 48, "fctm": 3.5, "fctk,0.05": 2.5, "fctk,0.95": 4.4, "Ecm": 35000},
            {"Grade": "C45/55", "fck": 45, "fcm": 53, "fctm": 3.8, "fctk,0.05": 2.7, "fctk,0.95": 4.9, "Ecm": 36000},
            {"Grade": "C50/60", "fck": 50, "fcm": 58, "fctm": 4.1, "fctk,0.05": 2.9, "fctk,0.95": 5.3, "Ecm": 37000},
        ]

        df_ec2 = pd.DataFrame(ec2_data)
        df_ec2["fcd"] = df_ec2["fck"] / 1.5  # Default γc = 1.5

        grade = st.selectbox("Select concrete grade (Eurocode):", df_ec2["Grade"], key="ec_grade")
        selected = df_ec2[df_ec2["Grade"] == grade].iloc[0]

        st.markdown("### ✅ Concrete properties (Eurocode):")
        st.write(f"**f<sub>ck</sub>** (Characteristic compressive strength, MPa): `{selected.fck}`", unsafe_allow_html=True)
        st.write(f"**f<sub>cm</sub>** (Mean compressive strength, MPa): `{selected.fcm}`", unsafe_allow_html=True)
        st.write(f"**f<sub>cd</sub>** (Design compressive strength, MPa): `{selected.fcd:.2f}`", unsafe_allow_html=True)
        st.write(f"**f<sub>ctm</sub>** (Mean tensile strength, MPa): `{selected.fctm}`", unsafe_allow_html=True)
        st.write(f"**f<sub>ctk,0.05</sub>** (5% fractile tensile strength): `{selected['fctk,0.05']}`", unsafe_allow_html=True)
        st.write(f"**f<sub>ctk,0.95</sub>** (95% fractile tensile strength): `{selected['fctk,0.95']}`", unsafe_allow_html=True)
        st.write(f"**E<sub>cm</sub>** (Modulus of elasticity, MPa): `{selected.Ecm}`", unsafe_allow_html=True)

        with st.expander("📘 Source"):
            st.markdown("Based on **EN 1992-1-1**, Section 3.1.2")

    # ========== TAB 2: CHINA ==========
    with tab2:
        st.subheader("🟥 Chinese Standard (GB 50010-2010)")

        cn_data = [
            {"Grade": "C20", "fcu": 20.1, "fc": 9.6, "ft": 1.27, "Ec": 27500},
            {"Grade": "C25", "fcu": 25.8, "fc": 11.9, "ft": 1.43, "Ec": 30000},
            {"Grade": "C30", "fcu": 31.0, "fc": 14.3, "ft": 1.57, "Ec": 32500},
            {"Grade": "C35", "fcu": 36.6, "fc": 16.7, "ft": 1.71, "Ec": 34500},
            {"Grade": "C40", "fcu": 41.4, "fc": 19.1, "ft": 1.80, "Ec": 36000},
            {"Grade": "C45", "fcu": 47.0, "fc": 21.2, "ft": 1.87, "Ec": 37000},
            {"Grade": "C50", "fcu": 52.0, "fc": 23.1, "ft": 1.96, "Ec": 38000},
        ]
        df_cn = pd.DataFrame(cn_data)

        grade_cn = st.selectbox("Select concrete grade (China):", df_cn["Grade"], key="cn_grade")
        selected_cn = df_cn[df_cn["Grade"] == grade_cn].iloc[0]

        st.markdown("### ✅ Concrete properties (China):")
        st.write(f"**f<sub>cu</sub>** (Cube compressive strength, MPa): `{selected_cn.fcu}`", unsafe_allow_html=True)
        st.write(f"**f<sub>c</sub>** (Axial compressive strength, MPa): `{selected_cn.fc}`", unsafe_allow_html=True)
        st.write(f"**f<sub>t</sub>** (Axial tensile strength, MPa): `{selected_cn.ft}`", unsafe_allow_html=True)
        st.write(f"**E<sub>c</sub>** (Elastic modulus, MPa): `{selected_cn.Ec}`", unsafe_allow_html=True)

        with st.expander("📘 Source"):
            st.markdown("Based on **GB 50010-2010**, Section 3.1 and Table 3.1.1")
