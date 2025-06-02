import streamlit as st
import pandas as pd

def run():
    st.header("📋 Bảng Tra Cường Độ Bê Tông theo Eurocode 2")

    # Dữ liệu bảng tra theo EC2
    data = [
        {"Cấp bền": "C20/25", "fck": 20, "fcm": 28, "fctm": 2.2, "fctk,0.05": 1.6, "fctk,0.95": 2.8, "Ecm": 30_000},
        {"Cấp bền": "C25/30", "fck": 25, "fcm": 33, "fctm": 2.6, "fctk,0.05": 1.9, "fctk,0.95": 3.3, "Ecm": 31_000},
        {"Cấp bền": "C30/37", "fck": 30, "fcm": 38, "fctm": 2.9, "fctk,0.05": 2.1, "fctk,0.95": 3.6, "Ecm": 32_000},
        {"Cấp bền": "C35/45", "fck": 35, "fcm": 43, "fctm": 3.2, "fctk,0.05": 2.3, "fctk,0.95": 4.1, "Ecm": 34_000},
        {"Cấp bền": "C40/50", "fck": 40, "fcm": 48, "fctm": 3.5, "fctk,0.05": 2.5, "fctk,0.95": 4.4, "Ecm": 35_000},
        {"Cấp bền": "C45/55", "fck": 45, "fcm": 53, "fctm": 3.8, "fctk,0.05": 2.7, "fctk,0.95": 4.9, "Ecm": 36_000},
        {"Cấp bền": "C50/60", "fck": 50, "fcm": 58, "fctm": 4.1, "fctk,0.05": 2.9, "fctk,0.95": 5.3, "Ecm": 37_000},
    ]
    df = pd.DataFrame(data)

    # Chọn cấp bền
    grade = st.selectbox("Chọn cấp độ bền bê tông:", df["Cấp bền"])

    selected = df[df["Cấp bền"] == grade].iloc[0]

    st.markdown("### ✅ Thông số cường độ:")
    st.write(f"**f<sub>ck</sub>** (đặc trưng nén, MPa): `{selected.fck}`", unsafe_allow_html=True)
    st.write(f"**f<sub>cm</sub>** (trung bình nén, MPa): `{selected.fcm}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctm</sub>** (trung bình kéo, MPa): `{selected.fctm}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctk,0.05</sub>** (kéo đặc trưng thấp, MPa): `{selected['fctk,0.05']}`", unsafe_allow_html=True)
    st.write(f"**f<sub>ctk,0.95</sub>** (kéo đặc trưng cao, MPa): `{selected['fctk,0.95']}`", unsafe_allow_html=True)
    st.write(f"**E<sub>cm</sub>** (mô đun đàn hồi, MPa): `{selected.Ecm}`", unsafe_allow_html=True)

    with st.expander("📘 Tham khảo"):
        st.markdown("Theo tiêu chuẩn **EN 1992-1-1 (Eurocode 2)**, mục 3.1.2")

